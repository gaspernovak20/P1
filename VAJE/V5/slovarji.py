
def zaloga(inventory, article):
    return inventory[article]

def prodaj(inventory, article, size):
    inventory[article] = inventory[article] - size

def primanjkljaj(inventory, order):

    inventory_more = {}
    for article, size in order.items():
        current_size = inventory.get(article, 0)
        if current_size < size:
            inventory_more[article] = size - current_size
    return inventory_more


def freq(s):
    c_count = {}
    for c in s:
        if c not in c_count:
            c_count[c] = 0
        c_count[c] += 1
    return c_count


def max_freq(f):
    return max(f, key=f.get)

def najpogostejse(s):
    word_count = {}
    for word in s.split():
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += 1

    return max_freq(word_count), max_freq(freq(s))

def nasledniki(txt):
    after = {}
    for word, word_after in pairwise(txt.split()):
        if word not in after:
            after[word] = []
        after[word].append(word_after)
    return after


# def tekst(nasl, num_besed):



def family_tree(family):
    children = {}
    for parent, child in family:
        if parent not in children:
            children[parent] = []
        children[parent].append(child)
    return children


def children(tree, name):
    return tree.get(name, [])

def grandchildren(tree, name):
    grandChildrenList = []
    for child in children(tree, name):
        grandChildrenList += children(tree, child)
    return grandChildrenList

def successors(tree, name):
    successorsList = []

    if name not in tree:
        return []

    for child in tree[name]:
        successorsList.append(child)
        successorsList += successors(tree, child)
    return successorsList

### ^^^ Naloge rešujte nad tem komentarjem. ^^^ ###

import unittest
import collections
from itertools import pairwise
class TestSlovarji(unittest.TestCase):
    def setUp(self):
        self.tree = {
            'alice': ['mary', 'tom', 'judy'],
            'bob': ['mary', 'tom', 'judy'],
            'ken': ['suzan'],
            'renee': ['rob', 'bob'],
            'rob': ['jim'],
            'sid': ['rob', 'bob'],
            'tom': ['ken']}

    def assertDictCounterEqual(self, first, second, msg=None):
        def dict_counter(d):
            d_copy = dict(d)
            for k, v in d_copy.items():
                d_copy[k] = collections.Counter(v)
            return d_copy
        self.assertDictEqual(dict_counter(first), dict_counter(second), msg)

    def test_zaloga(self):
        inv = {"kruh": 5, "kajzerica": 4, "makovka": 3}
        self.assertEqual(zaloga(inv, "kruh"), 5)
        self.assertEqual(zaloga(inv, "kajzerica"), 4)
        self.assertEqual(zaloga(inv, "makovka"), 3)

    def test_prodaj(self):
        inv = {"kruh": 5, "kajzerica": 4, "makovka": 3}
        self.assertIsNone(prodaj(inv, "kajzerica", 2), "Funkcija naj ne vrača ničesar!")
        self.assertEqual(zaloga(inv, "kruh"), 5)
        self.assertEqual(zaloga(inv, "kajzerica"), 2)
        self.assertEqual(zaloga(inv, "makovka"), 3)

        prodaj(inv, "kruh", 5)
        self.assertTrue("kruh" not in inv or (zaloga(inv, "kruh"), 0))
        self.assertEqual(zaloga(inv, "kajzerica"), 2)
        self.assertEqual(zaloga(inv, "makovka"), 3)

    def test_primanjkljaj(self):
        inventar = {
            'sir': 8, 'kruh': 15, 'makovka': 10, 'pasja radost': 2,
            'pašteta': 10, 'mortadela': 4, 'klobasa': 7
        }
        self.assertDictEqual(
            primanjkljaj(inventar, {"kruh": 2, "makovka": 10}),
            {})
        self.assertDictEqual(
            primanjkljaj(inventar, {"kruh": 2, "makovka": 12}),
            {"makovka": 2})
        self.assertDictEqual(
            primanjkljaj(inventar, {"kruh": 2, "makovka": 12, "pivo": 3}),
            {"makovka": 2, "pivo": 3})
        self.assertDictEqual(primanjkljaj(inventar, {}), {})
        self.assertDictEqual(primanjkljaj(inventar, inventar), {})

    def test_family_tree(self):
        family = [
            ('bob', 'mary'),
            ('bob', 'tom'),
            ('bob', 'judy'),
            ('alice', 'mary'),
            ('alice', 'tom'),
            ('alice', 'judy'),
            ('renee', 'rob'),
            ('renee', 'bob'),
            ('sid', 'rob'),
            ('sid', 'bob'),
            ('tom', 'ken'),
            ('ken', 'suzan'),
            ('rob', 'jim')]
        self.assertDictCounterEqual(family_tree(family), self.tree)

    def test_children(self):
        self.assertCountEqual(children(self.tree, 'alice'), ['mary', 'tom', 'judy'])
        self.assertCountEqual(children(self.tree, 'mary'), [])
        self.assertCountEqual(children(self.tree, 'renee'), ['bob', 'rob'])
        self.assertCountEqual(children(self.tree, 'rob'), ['jim'])
        self.assertCountEqual(children(self.tree, 'suzan'), [])

    def test_grandchildren(self):
        self.assertCountEqual(grandchildren(self.tree, 'alice'), ['ken'])
        self.assertCountEqual(grandchildren(self.tree, 'bob'), ['ken'])
        self.assertCountEqual(grandchildren(self.tree, 'ken'), [])
        self.assertCountEqual(grandchildren(self.tree, 'mary'), [])
        self.assertCountEqual(grandchildren(self.tree, 'renee'), ['jim', 'mary', 'tom', 'judy'])
        self.assertCountEqual(grandchildren(self.tree, 'sid'), ['jim', 'mary', 'tom', 'judy'])
        self.assertCountEqual(grandchildren(self.tree, 'tom'), ['suzan'])

    def test_successors(self):
        self.assertCountEqual(successors(self.tree, 'tom'), ['ken', 'suzan'])
        self.assertCountEqual(successors(self.tree, 'sid'),
            ['rob', 'bob', 'jim', 'mary', 'tom', 'judy', 'ken', 'suzan'])
        self.assertCountEqual(successors(self.tree, 'suzan'), [])
        self.assertCountEqual(successors(self.tree, 'ken'), ['suzan'])
        self.assertCountEqual(successors(self.tree, 'rob'), ['jim'])

    def test_najpogostejse(self):
        self.assertEqual(najpogostejse('a'), ('a', 'a'))
        self.assertEqual(najpogostejse('aa bb aa'), ('aa', 'a'))
        self.assertEqual(najpogostejse('in to in ono in to smo mi'), ('in', ' '))
        self.assertEqual(najpogostejse('abc abc abc abacbca'), ('abc', 'a'))
        self.assertEqual(najpogostejse('abc abc abc abacbcb'), ('abc', 'b'))
        self.assertEqual(najpogostejse('abc abc abc abacbcc'), ('abc', 'c'))

    def test_najpogostejse_urejene(self):
        self.assertEqual(najpogostejse_urejene('a'), (['a'], ['a']))
        self.assertEqual(najpogostejse_urejene('aa bb aa'), (['aa', 'bb'], ['a', ' ', 'b']))
        self.assertEqual(najpogostejse_urejene('in to in ono in to smo mi'),
            (['in', 'to', 'mi', 'ono', 'smo'], [' ', 'o', 'i', 'n', 'm', 't', 's']))
        self.assertEqual(najpogostejse_urejene('abc abc abc abacbca'),
            (['abc', 'abacbca'], ['a', 'b', 'c', ' ']))
        self.assertEqual(najpogostejse_urejene('abc abc abc abacbcb'),
            (['abc', 'abacbcb'], ['b', 'a', 'c', ' ']))
        self.assertEqual(najpogostejse_urejene('abc abc abc abacbcc'),
            (['abc', 'abacbcc'], ['c', 'a', 'b', ' ']))

    def test_sifra(self):
        self.assertEqual(sifra('\x19\x14\x1c]\x19\x0f\x14\t\x13\x18\t]\x12\x0e[\n\x1a\t\x18\x15\x12\x13\x1c'),
            'big brother is watching')
        self.assertEqual(sifra('\xe1d\xe0q\xe5r\xf7b\xe0i'), 'strawberry')

    def test_nasledniki(self):
        self.assertDictCounterEqual(nasledniki('in in in in'), {'in': ['in', 'in', 'in']})
        self.assertDictCounterEqual(nasledniki('in to in ono in to smo mi'),
            {'smo': ['mi'], 'to': ['in', 'smo'], 'ono': ['in'], 'in': ['to', 'ono', 'to']})
        self.assertDictCounterEqual(nasledniki('danes je lep dan danes sije sonce'),
            {'lep': ['dan'], 'je': ['lep'], 'dan': ['danes'], 'danes': ['je', 'sije'], 'sije': ['sonce']})

    def test_tekst(self):
        self.assertEqual(tekst({'in': ['in', 'in']}, 3), 'in in in')

if __name__ == '__main__':
    unittest.main(verbosity=2)
