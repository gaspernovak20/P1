def nabava(stari, novi):
    stare_ovire = collections.defaultdict(int)
    nove_ovire = collections.defaultdict(int)
    ovire_final = {}
    for st_ovira in stari:
        stare_ovire[st_ovira[1] - st_ovira[0] + 1] += 1
    for nv_ovira in novi:
        nove_ovire[nv_ovira[1] - nv_ovira[0] + 1] += 1
    for n_dolzina, n_kolicina in nove_ovire.items():
        for s_dolzina, s_kolicina in stare_ovire.items():
            if s_dolzina == n_dolzina and n_kolicina - s_kolicina > 0:
                ovire_final[s_dolzina] = n_kolicina - s_kolicina
    return ovire_final


def rekonstrukcija(kocke):
    ovire = []

    for i, (y, x) in enumerate(sorted(kocke)):
        izdelana_ovira = (x, x, y)
        if y == izdelana_ovira[2] and x - 1 == izdelana_ovira[1]:
            izdelana_ovira = izdelana_ovira[0], x, y
        else:
            ovire.append(izdelana_ovira)

    return ovire


def dekodiraj_vrstico(vrstica):
    ovire = []

    v_vrsatici = False

    for i, c in enumerate(vrstica, start=1):
        if c == '<':
            zacetek = i
        if c == '>' and i - zacetek + 1 != 1:
            ovire.append((zacetek, i))

    return ovire


def preberi(datoteka):
    zemljevid = []

    for i, vrstica in enumerate(open(datoteka, 'r'), start=1):
        for x0, x1 in dekodiraj_vrstico(vrstica):
            zemljevid.append((x0, x1, i))

    return zemljevid


def vrhovi(skladovnica, ovira, visina):
    vrh = set()

    if ovira not in skladovnica and visina <= 0:
        return {ovira}

    if ovira in skladovnica:
        for nad in skladovnica[ovira]:
            vrh |= vrhovi(skladovnica, nad, visina - 1)

    return vrh


class Ovire:
    def __init__(self, ovire):
        self.ovre = ovire
        self.zadetki = 0
        self.ovira_zadetki = collections.defaultdict(int)
        self.pobrisane = set()

    def strel(self, x, y):
        for x0, x1, y1 in self.ovre - self.pobrisane:
            if y == y1 and x0 <= x <= x1:
                self.zadetki += 1
                self.ovira_zadetki[(x0, x1, y1)] += 1
                if self.ovira_zadetki[(x0, x1, y1)] >= 3:
                    self.pobrisane.add((x0, x1, y1))
                return True
        return False

    def zadetkov(self):
        return self.zadetki

    def vse_ovire(self):
        return self.ovre - self.pobrisane

    def zmaga(self):
        return len(self.ovre - self.pobrisane) == 0


import unittest
import warnings
import random
import collections

with open("ovire.txt", "wt", encoding="utf-8") as f:
    f.write("""
...<-->........
<->......<--->.
...............
...<-->..<--->.
...............
...<-->........
<->..<>...<--->.
""".lstrip())


class Test(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    def test_1_nabava(self):
        self.assertEqual(nabava([], []), {})
        self.assertEqual(nabava([(1, 1, 1)], [(1, 1, 1)]), {})
        self.assertEqual(nabava([(1, 1, 1)], [(3, 3, 2)]), {})
        self.assertEqual(nabava([(5, 8, 3)], [(6, 9, 4)]), {})
        self.assertEqual(nabava([(1, 1, 1), (5, 8, 3)], [(3, 3, 8), (6, 9, 4)]), {})

        self.assertEqual(nabava([], [(1, 1, 2)]), {1: 1})
        self.assertEqual(nabava([], [(4, 8, 3)]), {5: 1})
        self.assertEqual(nabava([], [(1, 1, 2), (4, 8, 3)]), {1: 1, 5: 1})
        self.assertEqual(nabava([], [(1, 1, 2), (5, 9, 10), (4, 8, 3)]), {1: 1, 5: 2})
        self.assertEqual(nabava([(1, 1, 1)], [(1, 1, 2), (5, 9, 10), (4, 8, 3)]), {5: 2})
        self.assertEqual(nabava([], [(1, 1, 2), (10, 14, 7), (5, 9, 10), (4, 8, 3)]), {1: 1, 5: 3})
        self.assertEqual(nabava([(9, 13, 5)], [(1, 1, 2), (10, 14, 7), (5, 9, 10), (4, 8, 3)]), {1: 1, 5: 2})
        self.assertEqual(nabava([(1, 3, 1), (9, 13, 5)], [(1, 1, 2), (10, 14, 7), (5, 9, 10), (4, 8, 3)]), {1: 1, 5: 2})
        self.assertEqual(nabava([(1, 3, 1), (9, 13, 5)], [(1, 1, 2), (10, 14, 7), (5, 9, 10), (4, 8, 3)]), {1: 1, 5: 2})
        self.assertEqual(nabava([(1, 3, 1), (2, 2, 3), (9, 13, 5)], [(1, 1, 2), (10, 14, 7), (5, 9, 10), (4, 8, 3)]),
                         {5: 2})

    def test_2_rekonstrukcija(self):
        self.assertEqual([], rekonstrukcija([]))
        self.assertEqual(
            [(3, 3, 1)],
            rekonstrukcija([(1, 3)])
        )

        self.assertEqual(
            [(3, 4, 1)],
            rekonstrukcija([(1, 3), (1, 4)]))

        self.assertEqual(
            [(3, 4, 1)],
            rekonstrukcija([(1, 4), (1, 3)]))

        self.assertEqual(
            [(3, 5, 1)],
            rekonstrukcija([(1, 3), (1, 4), (1, 5)]))

        self.assertEqual(
            [(3, 5, 1)],
            rekonstrukcija([(1, 5), (1, 3), (1, 4)]))

        self.assertEqual(
            [(3, 5, 1), (3, 4, 2)],
            rekonstrukcija([(1, 5), (1, 3), (1, 4), (2, 3), (2, 4)]))

        self.assertEqual(
            [(3, 5, 1), (3, 4, 2)],
            rekonstrukcija([(1, 5), (1, 3), (1, 4), (2, 4), (2, 3)]))

        self.assertEqual(
            [(1, 2, 1), (2, 4, 2), (4, 4, 3)],
            rekonstrukcija([(1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4)]))
        # isto kot zgoraj, le pomešano
        self.assertEqual(
            [(1, 2, 1), (2, 4, 2), (4, 4, 3)],
            rekonstrukcija([(2, 3), (1, 1), (2, 2), (2, 4), (1, 2), (3, 4)]))

        self.assertEqual(
            [(1, 2, 1), (2, 4, 2), (4, 5, 3)],
            rekonstrukcija([(1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (3, 5)]))
        # isto kot zgoraj, le pomešano
        self.assertEqual(
            [(1, 2, 1), (2, 4, 2), (4, 5, 3)],
            rekonstrukcija([(3, 5), (1, 1), (2, 4), (3, 4), (1, 2), (2, 2), (2, 3)]))

        self.assertEqual(
            [(1, 2, 1), (2, 4, 2), (4, 5, 3), (5, 5, 4)],
            rekonstrukcija([(1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)]))
        # isto kot zgoraj, le pomešano
        self.assertEqual(
            [(1, 2, 1), (2, 4, 2), (4, 5, 3), (5, 5, 4)],
            rekonstrukcija([(1, 1), (2, 4), (3, 4), (1, 2), (2, 2), (2, 3), (3, 5), (4, 5)]))

        kocke = [(1, 2), (1, 3), (1, 4), (1, 8), (1, 9), (1, 10),
                 (2, 5),
                 (3, 2), (3, 3), (3, 4), (3, 8), (3, 9), (3, 10),
                 (4, 5),
                 (5, 1), (5, 2), (5, 3), (5, 7), (5, 8), (5, 9),
                 (6, 4),
                 (7, 1), (7, 2), (7, 3), (7, 7), (7, 8), (7, 9)]

        for _ in range(10):
            random.shuffle(kocke)
            self.assertEqual(
                [(2, 4, 1), (8, 10, 1), (5, 5, 2), (2, 4, 3), (8, 10, 3), (5, 5, 4),
                 (1, 3, 5), (7, 9, 5), (4, 4, 6), (1, 3, 7), (7, 9, 7)],
                rekonstrukcija(kocke))

    def test_3a_dekodiraj_vrstico(self):
        self.assertEqual([], dekodiraj_vrstico("........"))
        self.assertEqual([(1, 2)], dekodiraj_vrstico("<>......"))
        self.assertEqual([(3, 4)], dekodiraj_vrstico("..<>......"))
        self.assertEqual([(3, 6)], dekodiraj_vrstico("..<-->....."))
        self.assertEqual([(3, 6), (10, 15)], dekodiraj_vrstico("..<-->...<---->.."))
        self.assertEqual([(3, 6), (10, 15), (18, 19)], dekodiraj_vrstico("..<-->...<---->..<>"))
        self.assertEqual([(1, 2), (4, 7), (11, 16), (19, 20)], dekodiraj_vrstico("<>.<-->...<---->..<>"))

    def test_3b_preberi(self):
        self.assertEqual([(4, 7, 1),
                          (1, 3, 2),
                          (10, 14, 2),
                          (4, 7, 4),
                          (10, 14, 4),
                          (4, 7, 6),
                          (1, 3, 7),
                          (6, 7, 7),
                          (11, 15, 7)], preberi("ovire.txt"))

    def test_4_vrhovi(self):
        """
               T
          j    l         z      B  A
          w i oo  pp     s      gg n
          c r uu vvv     x y    qq mm
          aaa bbbbbb     ttt ee fffff
          dddddddddd     hhhhhhhhhhhh
        ..............................
        """
        skladovnica = {
            ".": "dh",
            "d": "ab",
            "h": "tef",
            "a": "cr",
            "b": "uv",
            "t": "xy",
            "f": "qm",
            "c": "w",
            "r": "i",
            "u": "o",
            "v": "p",
            "x": "s",
            "y": "",
            "q": "g",
            "m": "n",
            "w": "j",
            "o": "l",
            "s": "z",
            "g": "B",
            "n": "A",
            "l": "T"
        }
        self.assertEqual(set("jiTp"), vrhovi(skladovnica, "d", 0))
        self.assertEqual(set("jiTp"), vrhovi(skladovnica, "d", -2))
        self.assertEqual(set("jiTp"), vrhovi(skladovnica, "d", 3))
        self.assertEqual(set("jT"), vrhovi(skladovnica, "d", 4))
        self.assertEqual(set("T"), vrhovi(skladovnica, "d", 5))
        self.assertEqual(set(), vrhovi(skladovnica, "d", 6))

        self.assertEqual(set("T"), vrhovi(skladovnica, "u", 2))
        self.assertEqual(set("Tp"), vrhovi(skladovnica, "b", 2))
        self.assertEqual(set("T"), vrhovi(skladovnica, "b", 3))

        self.assertEqual({'i', 'A', 'p', 'T', 'B', 'z', 'j', 'e'}, vrhovi(skladovnica, ".", 2))
        self.assertEqual({'i', 'A', 'p', 'T', 'B', 'z', 'j'}, vrhovi(skladovnica, ".", 3))
        self.assertEqual({'i', 'A', 'p', 'T', 'B', 'z', 'j'}, vrhovi(skladovnica, ".", 4))
        self.assertEqual({'A', 'T', 'B', 'z', 'j'}, vrhovi(skladovnica, ".", 5))
        self.assertEqual({'T'}, vrhovi(skladovnica, ".", 6))
        self.assertEqual(set(), vrhovi(skladovnica, ".", 7))

    def test_5_potapljanje(self):
        zacetne = {(1, 2, 5), (2, 4, 2), (5, 10, 4)}
        kopija = zacetne.copy()
        ovire = Ovire(zacetne)
        self.assertEqual(zacetne, ovire.vse_ovire())
        self.assertEqual(0, ovire.zadetkov())

        ovire2 = Ovire(set())
        self.assertEqual(0, ovire2.zadetkov())
        self.assertEqual(set(), ovire2.vse_ovire())
        self.assertTrue(ovire2.zmaga())

        self.assertFalse(ovire.strel(1, 1))
        self.assertEqual(zacetne, ovire.vse_ovire())
        self.assertEqual(0, ovire.zadetkov())

        self.assertTrue(ovire.strel(3, 2))
        self.assertEqual(zacetne, ovire.vse_ovire())
        self.assertEqual(1, ovire.zadetkov())
        self.assertFalse(ovire.zmaga())

        self.assertTrue(ovire.strel(2, 5))
        self.assertEqual(zacetne, ovire.vse_ovire())
        self.assertEqual(2, ovire.zadetkov())

        self.assertTrue(ovire.strel(3, 2))
        self.assertEqual(zacetne, ovire.vse_ovire())
        self.assertEqual(3, ovire.zadetkov())

        self.assertTrue(ovire.strel(4, 2))
        self.assertEqual({(1, 2, 5), (5, 10, 4)}, ovire.vse_ovire())
        self.assertEqual(4, ovire.zadetkov())

        self.assertFalse(ovire.strel(4, 2))
        self.assertEqual({(1, 2, 5), (5, 10, 4)}, ovire.vse_ovire())
        self.assertEqual(4, ovire.zadetkov())

        self.assertFalse(ovire.strel(2, 2))
        self.assertEqual({(1, 2, 5), (5, 10, 4)}, ovire.vse_ovire())
        self.assertEqual(4, ovire.zadetkov())

        self.assertFalse(ovire.zmaga())
        self.assertEqual(kopija, zacetne)

        self.assertEqual(0, ovire2.zadetkov())
        self.assertEqual(set(), ovire2.vse_ovire())
        self.assertTrue(ovire2.zmaga())

        self.assertTrue(ovire.strel(5, 4))
        self.assertEqual({(1, 2, 5), (5, 10, 4)}, ovire.vse_ovire())
        self.assertEqual(5, ovire.zadetkov())

        self.assertTrue(ovire.strel(10, 4))
        self.assertEqual({(1, 2, 5), (5, 10, 4)}, ovire.vse_ovire())
        self.assertEqual(6, ovire.zadetkov())

        self.assertFalse(ovire.strel(4, 2))
        self.assertEqual({(1, 2, 5), (5, 10, 4)}, ovire.vse_ovire())
        self.assertEqual(6, ovire.zadetkov())

        self.assertTrue(ovire.strel(1, 5))
        self.assertEqual({(1, 2, 5), (5, 10, 4)}, ovire.vse_ovire())
        self.assertEqual(7, ovire.zadetkov())

        self.assertTrue(ovire.strel(1, 5))
        self.assertEqual({(5, 10, 4)}, ovire.vse_ovire())
        self.assertEqual(8, ovire.zadetkov())

        self.assertFalse(ovire.strel(1, 5))
        self.assertEqual({(5, 10, 4)}, ovire.vse_ovire())
        self.assertEqual(8, ovire.zadetkov())

        self.assertFalse(ovire.zmaga())

        self.assertTrue(ovire.strel(7, 4))
        self.assertEqual(set(), ovire.vse_ovire())
        self.assertEqual(9, ovire.zadetkov())

        self.assertTrue(ovire.zmaga())

        self.assertFalse(ovire.strel(7, 4))
        self.assertEqual(set(), ovire.vse_ovire())
        self.assertEqual(9, ovire.zadetkov())

        self.assertTrue(ovire.zmaga())

        self.assertEqual(0, ovire2.zadetkov())
        self.assertEqual(set(), ovire2.vse_ovire())
        self.assertTrue(ovire2.zmaga())


if __name__ == "__main__":
    unittest.main()
