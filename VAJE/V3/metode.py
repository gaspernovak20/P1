import unittest
import itertools

def unikati(s):

    all_elements = []
    for element in s:
        if element not in all_elements:
            all_elements.append(element)

    return all_elements

def avtor(twit):
    return twit.split(":")[0]

def vsi_avtorji(twits):

    all_authors = []
    for twit in twits:
        all_authors.append(avtor(twit))
    return unikati(all_authors)


def izloci_besedo(word):

    while word and not word[0].isalnum():
        word = word[1:]
    while word and not word[len(word)-1].isalnum():
        word = word[:len(word)-1]
    return word


def se_zacne_z(twit, c):
    starts_with = []
    for word in twit.split():
        if word.startswith(c):
            starts_with.append(izloci_besedo(word))
    return starts_with


def zberi_se_zacne_z(twits, c):
    starts_with = []
    for twit in twits:
        starts_with += se_zacne_z(twit, c)
    return unikati(starts_with)


def vse_afne(twits):
    return zberi_se_zacne_z(twits, "@")


def vsi_hashtagi(twits):
    return zberi_se_zacne_z(twits, "#")

def vse_osebe(twits):
    return sorted(unikati(vsi_avtorji(twits) + vse_afne(twits)))


def custva(twits, hashtags):
    # authors = []
    # for twit in twits:
    #     for used_hash in se_zacne_z(twit, "#"):
    #         if used_hash in hashtags:
    #             authors.append(avtor(twit))
    #             break
    # return sorted(unikati(authors))
    return unikati(sorted(avtor(twit) for twit in twits if set(hashtags) & set(se_zacne_z(twit, "#"))))


def se_poznata(twits, oseba1, oseba2):
    # known_people = []
    # for twit in twits:
    #     if oseba1 == avtor(twit) or oseba2 == avtor(twit):
    #         known_people += se_zacne_z(twit, "@")
    #
    # return oseba1 in known_people or oseba2 in known_people
    for twit in twits:
        author = avtor(twit)
        known = se_zacne_z(twit, "@")
        if author == oseba1 and oseba2 in known or author == oseba2 and oseba1 in known:
            return True

class TestTviti(unittest.TestCase):
    tviti = [
        "sandra: Spet ta dež. #dougcajt",
        "berta: @sandra Delaj domačo za #programiranje1",
        "sandra: @berta Ne maram #programiranje1 #krneki",
        "ana: kdo so te @berta, @cilka, @dani? #krneki",
        "cilka: jst sm pa #luft",
        "benjamin: pogrešam ano #zalosten",
        "ema: @benjamin @ana #split? po dvopičju, za začetek?",
    ]



    def test_01_unikat(self):
        self.assertEqual(unikati([1, 2, 1, 1, 3, 2]), [1, 2, 3])
        self.assertEqual(unikati([1, 3, 2, 1, 1, 3, 2]), [1, 3, 2])
        self.assertEqual(unikati([1, 5, 4, 3, 2]), [1, 5, 4, 3, 2])
        self.assertEqual(unikati([1, 1, 1, 1, 1]), [1])
        self.assertEqual(unikati([1]), [1])
        self.assertEqual(unikati([]), [])
        self.assertEqual(unikati(["Ana", "Berta", "Cilka", "Berta"]), ["Ana", "Berta", "Cilka"])

    def test_02_avtor(self):
        self.assertEqual(avtor("janez: pred dvopičjem avtor, potem besedilo"), "janez")
        self.assertEqual(avtor("ana: malo krajse ime"), "ana")
        self.assertEqual(avtor("benjamin: pomembne so tri stvari: prva, druga in tretja"), "benjamin")

    def test_03_vsi_avtorji(self):
        self.assertEqual(vsi_avtorji(self.tviti), ["sandra", "berta", "ana", "cilka", "benjamin", "ema"])
        self.assertEqual(vsi_avtorji(self.tviti[:3]), ["sandra", "berta"])

    def test_04_izloci_besedo(self):
        self.assertEqual(izloci_besedo("@ana"), "ana")
        self.assertEqual(izloci_besedo("@@ana!!!"), "ana")
        self.assertEqual(izloci_besedo("ana"), "ana")
        self.assertEqual(izloci_besedo("!#$%\"=%/%()/Ben-jamin'"), "Ben-jamin")

    def test_05_vse_na_crko(self):
        self.assertEqual(se_zacne_z("Benjamin $je $skocil! Visoko!", "$"), ["je", "skocil"])
        self.assertEqual(se_zacne_z("Benjamin $je $skocil! #Visoko!", "$"), ["je", "skocil"])
        self.assertEqual(se_zacne_z("ana: kdo so te @berta, @cilka, @dani? #krneki", "@"), ["berta", "cilka", "dani"])

    def test_06_zberi_na_crko(self):
        self.assertEqual(zberi_se_zacne_z(self.tviti, "@"), ['sandra', 'berta', 'cilka', 'dani', 'benjamin', 'ana'])
        self.assertEqual(zberi_se_zacne_z(self.tviti, "#"), ['dougcajt', 'programiranje1', 'krneki', 'luft', 'zalosten', 'split'])

    def test_07_vse_afne(self):
        self.assertEqual(vse_afne(self.tviti), ['sandra', 'berta', 'cilka', 'dani', 'benjamin', 'ana'])

    def test_08_vsi_hashtagi(self):
        self.assertEqual(vsi_hashtagi(self.tviti), ['dougcajt', 'programiranje1', 'krneki', 'luft', 'zalosten', 'split'])

    def test_09_vse_osebe(self):
        self.assertEqual(vse_osebe(self.tviti), ['ana', 'benjamin', 'berta', 'cilka', 'dani', 'ema', 'sandra'])

    def test_10_custva(self):
        self.assertEqual(custva(self.tviti, ["dougcajt", "krneki"]), ["ana", "sandra"])
        self.assertEqual(custva(self.tviti, ["luft"]), ["cilka"])
        self.assertEqual(custva(self.tviti, ["meh"]), [])

    def test_11_se_poznata(self):
        self.assertTrue(se_poznata(self.tviti, "ana", "berta"))
        self.assertTrue(se_poznata(self.tviti, "ema", "ana"))
        self.assertFalse(se_poznata(self.tviti, "sandra", "ana"))
        self.assertFalse(se_poznata(self.tviti, "cilka", "luft"))
        self.assertFalse(se_poznata(self.tviti, "cilka", "balon"))


if __name__ == "__main__":
    unittest.main()

