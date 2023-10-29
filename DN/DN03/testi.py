import unittest


def dolzina_ovir(vrstica):
    st_ovir = 0
    for c in vrstica:
        if c == "#":
            st_ovir += 1

    return st_ovir


def stevilo_ovir(vrstica):
    st_ovir = 0
    znana_ovira = False
    for c in vrstica:
        if c == "#" and not znana_ovira:
            st_ovir += 1
            znana_ovira = True

        if c == "." and znana_ovira:
            znana_ovira = False

    return st_ovir

def najsirsa_ovira(vrstica):
    len_najsirse_ovira = 0
    len_ovira = 0

    znana_ovira = False
    for i in range(len(vrstica)):

        c = vrstica[i]
        # zacetek nove ovre
        if c == "#" and not znana_ovira:
            len_ovira = 1
            znana_ovira = True
            continue

        # kontrola dolzine ovire
        if c == "#" and znana_ovira:
            len_ovira += 1

        # konec ovire
        if (c == "." and znana_ovira) or i == (len(vrstica) - 1):
            # previrimo ali je prejsnja ovira najdaljsa znana ovira do sedaj
            if len_najsirse_ovira < len_ovira:
                len_najsirse_ovira = len_ovira
        znana_ovira = False

    return len_najsirse_ovira


def pretvori_vrstico(vrstica):
    seznam_parov = []
    zacetek_ovire = 0

    znana_ovira = False
    for i, c in enumerate(vrstica):

        if c == "#" and not znana_ovira:
            zacetek_ovire = i + 1
            znana_ovira = True

        if c == "." and znana_ovira:
            seznam_parov.append((zacetek_ovire, i))
            znana_ovira = False

        if znana_ovira and i == len(vrstica) - 1:
            seznam_parov.append((zacetek_ovire, i+1))

    return seznam_parov


def pretvori_zemljevid(vrstice):
    seznam_ovir = []
    for i, vrstica in enumerate(vrstice):
        for ovira_kordinate in pretvori_vrstico(vrstica):
            seznam_ovir.append(ovira_kordinate + (i + 1,))

    return seznam_ovir


def izboljsave(prej, potem):
    ovire_prej = pretvori_zemljevid(prej)
    ovire_potem = pretvori_zemljevid(potem)

    nove_ovire = []

    for ovira in ovire_potem:
        if ovira in ovire_prej:
            continue
        else:
            nove_ovire.append(ovira)

    return nove_ovire


def huligani(prej, potem):
    nove_ovire = izboljsave(prej, potem)

    ukradene_ovire = izboljsave(potem, prej)

    return nove_ovire, ukradene_ovire
class Test(unittest.TestCase):
    def test_dolzina_ovir(self):
        self.assertEqual(3, dolzina_ovir("...###..."))
        self.assertEqual(1, dolzina_ovir("...#..."))
        self.assertEqual(2, dolzina_ovir("...#..#."))
        self.assertEqual(7, dolzina_ovir("#...#####..#."))
        self.assertEqual(8, dolzina_ovir("...#####.##...#"))
        self.assertEqual(9, dolzina_ovir("#...#####.##...#"))
        self.assertEqual(6, dolzina_ovir("##...#.#...##"))
        self.assertEqual(0, dolzina_ovir("..."))
        self.assertEqual(0, dolzina_ovir("."))

    def test_stevilo_ovir(self):
        self.assertEqual(1, stevilo_ovir("...###..."))
        self.assertEqual(1, stevilo_ovir("...#..."))
        self.assertEqual(2, stevilo_ovir("...#..#."))
        self.assertEqual(3, stevilo_ovir("#...#####..#."))
        self.assertEqual(3, stevilo_ovir("...#####.##...#"))
        self.assertEqual(4, stevilo_ovir("#...#####.##...#"))
        self.assertEqual(4, stevilo_ovir("##...#.#...##"))
        self.assertEqual(0, stevilo_ovir("..."))
        self.assertEqual(0, stevilo_ovir("."))

    def test_najsirsa_ovira(self):
        self.assertEqual(3, najsirsa_ovira("...###..."))
        self.assertEqual(1, najsirsa_ovira("...#..."))
        self.assertEqual(1, najsirsa_ovira("...#..#."))
        self.assertEqual(5, najsirsa_ovira("#...#####..#."))
        self.assertEqual(5, najsirsa_ovira("...#####.##...#"))
        self.assertEqual(5, najsirsa_ovira("#...#####.##...#"))
        self.assertEqual(6, najsirsa_ovira("######...#####.##...#"))
        self.assertEqual(6, najsirsa_ovira("...#####.##...######"))

    def test_pretvori_vrstico(self):
        self.assertEqual([(3, 5)], pretvori_vrstico("..###."))
        self.assertEqual([(3, 5), (7, 7)], pretvori_vrstico("..###.#."))
        self.assertEqual([(1, 2), (5, 7), (9, 9)], pretvori_vrstico("##..###.#."))
        self.assertEqual([(1, 1), (4, 6), (8, 8)], pretvori_vrstico("#..###.#."))
        self.assertEqual([(1, 1), (4, 6), (8, 8)], pretvori_vrstico("#..###.#"))
        self.assertEqual([], pretvori_vrstico("..."))
        self.assertEqual([], pretvori_vrstico(".."))
        self.assertEqual([], pretvori_vrstico("."))

    def test_pretvori_zemljevid(self):
        zemljevid = [
            "......",
            "..##..",
            ".##.#.",
            "...###",
            "###.##",
        ]
        self.assertEqual([(3, 4, 2), (2, 3, 3), (5, 5, 3), (4, 6, 4), (1, 3, 5), (5, 6, 5)], pretvori_zemljevid(zemljevid))
    
        zemljevid = [
            "..............##...",
            "..###.....###....##",
            "...###...###...#...",
            "...........#.....##",
            "...................",
            "###.....#####...###"
        ]
        self.assertEqual([(15, 16, 1),
                          (3, 5, 2), (11, 13, 2), (18, 19, 2),
                          (4, 6, 3), (10, 12, 3), (16, 16, 3),
                          (12, 12, 4), (18, 19, 4),
                          (1, 3, 6), (9, 13, 6), (17, 19, 6)], pretvori_zemljevid(zemljevid))

    def test_izboljsave(self):
        prej = [
            "..............##...",
            "..###.....###....##",
            "...###...###...#...",
            "...........#.....##",
            "...................",
            "###.....#####...###"
        ]

        potem = [
            "...##.........##...",
            "..###.....###....##",
            "#..###...###...#...",
            "...###.....#.....##",
            "................###",
            "###.....#####...###"
        ]

        self.assertEqual([(4, 5, 1), (1, 1, 3), (4, 6, 4), (17, 19, 5)], izboljsave(prej, potem))

        self.assertEqual([], izboljsave(prej, prej))

    def test_huligani(self):
        prej = [
            "..............##...",
            "..###.....###....##",
            "...###...###...#...",
            "...........#.....##",
            "...................",
            "###.....#####...###"
        ]

        potem = [
            "...##..............",
            "..........###....##",
            "#..###...###...#...",
            "...###.....#.....##",
            "................###",
            "###.....##.##...###"
        ]

        dodane, odstranjene = huligani(prej, potem)
        self.assertEqual([(4, 5, 1), (1, 1, 3), (4, 6, 4), (17, 19, 5), (9, 10, 6), (12, 13, 6)], dodane, "Napaka v seznamu dodanih")
        self.assertEqual([(15, 16, 1), (3, 5, 2), (9, 13, 6)], odstranjene, "Napaka v seznamu odstranjenih")

        dodane, odstranjene = huligani(potem, prej)  # Pazi, obrnjeno!
        self.assertEqual([(15, 16, 1), (3, 5, 2), (9, 13, 6)], dodane, "Napaka v seznamu dodanih")
        self.assertEqual([(4, 5, 1), (1, 1, 3), (4, 6, 4), (17, 19, 5), (9, 10, 6), (12, 13, 6)], odstranjene, "Napaka v seznamu odstranjenih")

        self.assertEqual(([], []), huligani(prej, prej))


if __name__ == "__main__":
    unittest.main()
