def cas_za_povezavo(povezava, pribitki):
    return 4 + sum(pribitki.get(obstacle, 0) for obstacle in zemljevid[povezava])


def cas(pot, pribitki):
    return sum(cas_za_povezavo(connection, pribitki) for connection in pairwise(pot))


def povezava_spotike(pribitki):
    max_key = None
    max_val = None
    for connection in zemljevid:
        connection_time = cas_za_povezavo(connection, pribitki)
        if max_val is None or max_val <= connection_time:
            max_key = connection
            max_val = connection_time

    return max_key


def urnik(pot, pribitki):
    time = 0
    urnik = {pot[0]: time}
    for start, finish in pairwise(pot):
        time += cas_za_povezavo((start, finish), pribitki)
        if finish not in urnik:
            urnik[finish] = time

    return urnik


def skupinski_sport(pot, pribitkii):
    time = 0
    for connection in pairwise(pot):
        time += max(cas_za_povezavo(connection, pribitek) for pribitek in pribitkii)

    return time


def tekma(pot, pribitkii):
    times = [cas(pot, pribitek) for pribitek in pribitkii]
    first_min = None
    secound_min = None

    for i, time in enumerate(times):
        if first_min == None or times[first_min] >= time:
            secound_min = first_min
            first_min = i

    if secound_min != None and times[first_min] == times[secound_min]:
        return None

    return first_min


def trening(pot, pribitki):
    time = 0
    for connection in pairwise(pot):
        time += cas_za_povezavo(connection, pribitki)
        for obstacle in zemljevid[connection]:
            pribitki[obstacle] *= 0.95
    return time


def zastavice(pot, pribitkii):
    known_intersections = set()
    flags = [0] * len(pribitkii)
    flags[0] = 1

    inner_path = pot[0]
    for intersection in pot[1:]:
        inner_path += intersection
        if intersection not in known_intersections:
            known_intersections.add(intersection)
            flags[np.argmin([cas(inner_path, pribitek) for pribitek in pribitkii])] += 1

    return flags


def cikel(zacetna_tocka, pribitki):
    path = [zacetna_tocka]

    prev_intersection = zacetna_tocka
    current_intersection = zacetna_tocka

    while len(path) <= (2 * 21 + 1):
        available_intersections = [end
                                   for (start, end), obstacles in zemljevid.items()
                                   if start == current_intersection and end != prev_intersection]

        # print(path[-1], current_intersection, available_intersections)
        next_intersection_i = np.argmin([
            cas_za_povezavo((current_intersection, possible), pribitki)
            for possible in available_intersections])

        next_intersection = available_intersections[next_intersection_i]

        path.append(next_intersection)
        current_intersection = next_intersection
        prev_intersection = path[-2]

    # iskanje loopa
    known = set()

    # gremo iz konca proti zacetku
    # ker vemo da smo na konc zagotovo ze v loopu
    for intersection in path[::-1]:
        if intersection not in known:
            known.add(intersection)
        else:
            break

    return len(known)


# def izpadanje(poti, pribitkii):
    

import unittest
from itertools import pairwise
import numpy as np

A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, R, S, T, U, V = "ABCDEFGHIJKLMNOPRSTUV"

zemljevid = {
    (A, B): {'trava', 'gravel'},
    (B, A): {'trava', 'gravel'},
    (A, V): {'lonci', 'pešci'},
    (V, A): {'lonci', 'pešci'},
    (B, C): {'lonci', 'bolt'},
    (C, B): {'lonci', 'bolt'},
    (B, V): set(),
    (V, B): set(),
    (C, R): {'lonci', 'pešci', 'stopnice'},
    (R, C): {'lonci', 'pešci', 'stopnice'},
    (D, F): {'pešci', 'stopnice'},
    (F, D): {'pešci', 'stopnice'},
    (D, R): {'pešci'},
    (R, D): {'pešci'},
    (E, I): {'lonci', 'trava'},
    (I, E): {'lonci', 'trava'},
    (F, G): {'črepinje', 'trava'},
    (G, F): {'črepinje', 'trava'},
    (G, H): {'pešci', 'črepinje'},
    (H, G): {'pešci', 'črepinje'},
    (G, I): {'avtocesta'},
    (I, G): {'avtocesta'},
    (H, J): {'bolt', 'robnik'},
    (J, H): {'bolt', 'robnik'},
    (I, M): {'avtocesta'},
    (M, I): {'avtocesta'},
    (I, P): {'gravel'},
    (P, I): {'gravel'},
    (I, R): {'stopnice', 'robnik'},
    (R, I): {'stopnice', 'robnik'},
    (J, K): set(),
    (K, J): set(),
    (J, L): {'bolt', 'gravel'},
    (L, J): {'bolt', 'gravel'},
    (K, M): {'bolt', 'stopnice'},
    (M, K): {'bolt', 'stopnice'},
    (L, M): {'pešci', 'robnik'},
    (M, L): {'pešci', 'robnik'},
    (M, N): {'rodeo'},
    (N, M): {'rodeo'},
    (N, P): {'gravel'},
    (P, N): {'gravel'},
    (O, P): {'gravel'},
    (P, O): {'gravel'},
    (P, S): set(),
    (S, P): set(),
    (R, U): {'pešci', 'trava'},
    (U, R): {'pešci', 'trava'},
    (R, V): {'lonci', 'pešci'},
    (V, R): {'lonci', 'pešci'},
    (S, T): {'robnik', 'trava'},
    (T, S): {'robnik', 'trava'},
    (T, U): {'trava', 'gravel'},
    (U, T): {'trava', 'gravel'},
    (U, V): {'lonci', 'robnik', 'trava'},
    (V, U): {'lonci', 'robnik', 'trava'}
}

pribitki1 = dict(gravel=2, trava=3, lonci=1, bolt=2, pešci=4,
                 stopnice=3, avtocesta=5, črepinje=1, robnik=1,
                 rodeo=4)

pribitki2 = dict(gravel=2, trava=3, lonci=1, bolt=100, pešci=4,
                 stopnice=3, avtocesta=5, črepinje=1, robnik=1,
                 rodeo=4)

pribitki3 = dict(gravel=2, trava=3, lonci=100, bolt=2, pešci=4,
                 stopnice=3, avtocesta=5, črepinje=1, robnik=1,
                 rodeo=4)

pribitki4 = dict(gravel=2, trava=3, lonci=1, bolt=2, pešci=100,
                 stopnice=3, avtocesta=5, črepinje=1, robnik=1,
                 rodeo=4)


class Test06(unittest.TestCase):
    def test_01_cas_za_povezavo(self):
        self.assertEqual(4 + 1 + 2, cas_za_povezavo((A, B), dict(gravel=1, trava=2, robnik=3, avtocesta=5, bolt=2)))
        self.assertEqual(4 + 2 + 2, cas_za_povezavo((H, J), dict(gravel=1, trava=2, robnik=2, avtocesta=5, bolt=2)))
        self.assertEqual(4 + 5, cas_za_povezavo((G, I), dict(gravel=1, trava=2, robnik=3, avtocesta=5, bolt=2)))
        self.assertEqual(4, cas_za_povezavo((S, P), dict(gravel=1, trava=2, robnik=3, avtocesta=5, bolt=2)))
        self.assertEqual(4 + 2 + 3, cas_za_povezavo((A, B), pribitki1))
        self.assertEqual(4 + 2 + 1, cas_za_povezavo((B, C), pribitki1))
        self.assertEqual(4 + 3 + 5, cas_za_povezavo((C, R), pribitki1))
        self.assertEqual(4 + 4, cas_za_povezavo((R, D), pribitki1))
        self.assertEqual(4 + 3 + 4, cas_za_povezavo((D, F), pribitki1))
        self.assertEqual(4 + 3 + 1, cas_za_povezavo((F, G), pribitki1))

    def test_02_cas(self):
        self.assertEqual(9 + 7 + 3 * 12 + 8 + 11 + 8, cas("ABCRCRDFG", pribitki1))
        self.assertEqual(9, cas("AB", pribitki1))
        self.assertEqual(7, cas("AB", dict(gravel=1, trava=2, robnik=3, avtocesta=5, bolt=2)))
        self.assertEqual(7 + 21, cas("ABC", dict(gravel=1, trava=2, robnik=3, avtocesta=5, bolt=2, lonci=15)))
        self.assertEqual(8, cas("SPS", dict(gravel=1, trava=2, robnik=3, avtocesta=5, bolt=2, lonci=15)))

    def test_03_povezava_spotike(self):
        self.assertEqual((R, C), povezava_spotike(pribitki1))
        pribitki = pribitki1.copy()
        pribitki["avtocesta"] = 100
        self.assertEqual((M, I), povezava_spotike(pribitki))

        pribitki = dict.fromkeys(pribitki1, 0)  # vsi pribitki so 0, razen:
        pribitki["staopnice"] = pribitki["bolt"] = 1
        self.assertEqual((M, K), povezava_spotike(pribitki))


class Test07(unittest.TestCase):
    def test_01_urnik(self):
        self.assertEqual(dict(A=0, B=9, C=16, R=28, D=60, F=71, G=79), urnik("ABCRCRDFG", pribitki1))

        pribitki = dict.fromkeys(pribitki1, 0)  # vsi pribitki so 0, razen:
        self.assertEqual(dict(A=0, B=4, C=8, R=12, D=24, F=28, G=32), urnik("ABCRCRDFG", pribitki))

        pribitki["lonci"] = 1
        self.assertEqual(dict(A=0, B=4, C=9, R=14, D=28, F=32, G=36), urnik("ABCRCRDFG", pribitki))

    def test_02_skupinski_sport(self):
        self.assertEqual(9 + 7 + 3 * 12 + 8 + 11 + 8, skupinski_sport("ABCRCRDFG", [pribitki1]))
        self.assertEqual(177, skupinski_sport("ABCRCRDFG", [pribitki1, pribitki2]))
        self.assertEqual(177, skupinski_sport("ABCRCRDFG", [pribitki1, pribitki2, pribitki2]))
        self.assertEqual(475, skupinski_sport("ABCRCRDFG", [pribitki1, pribitki2, pribitki2, pribitki3]))

    def test_03_tekma(self):
        # pribitki1 je hitrejši od pribitki2, pribitki2 je hitrejši od pribitki3
        self.assertEqual(0, tekma("ABCRDF", [pribitki2]))
        self.assertEqual(0, tekma("ABCRDF", [pribitki2, pribitki3]))
        self.assertEqual(1, tekma("ABCRDF", [pribitki3, pribitki2]))
        self.assertEqual(2, tekma("ABCRDF", [pribitki3, pribitki2, pribitki1]))
        self.assertIsNone(tekma("ABCRDF", [pribitki1, pribitki2, pribitki1]))
        self.assertIsNone(tekma("ABCRDF", [pribitki3, pribitki1, pribitki2, pribitki1]))
        self.assertIsNone(tekma("ABCRDF", [pribitki3, pribitki1, pribitki1, pribitki2]))
        self.assertEqual(0, tekma("ABCRDF", [pribitki1, pribitki2, pribitki2]))
        self.assertEqual(1, tekma("ABCRDF", [pribitki2, pribitki1, pribitki2]))
        self.assertEqual(2, tekma("ABCRDF", [pribitki2, pribitki2, pribitki1]))


class Test08(unittest.TestCase):
    def test_01_trening(self):
        pribitki = pribitki1.copy()
        self.assertAlmostEqual(4 + 2 + 3, trening("AB", pribitki))

        pribitki = pribitki1.copy()
        self.assertAlmostEqual(4 + 2 + 3 + 4 + 2 * 0.95 + 3 * 0.95, trening("ABA", pribitki))

        pribitki = pribitki1.copy()
        self.assertAlmostEqual(4 + 2 + 3, trening("AB", pribitki))
        self.assertAlmostEqual(4 + 2 * 0.95 + 3 * 0.95, trening("BA", pribitki),
                               "Je nekdo pozabil spremeniti `pribitki`?")

        pribitki = pribitki1.copy()
        self.assertAlmostEqual(75.787025, trening("ABCRCRDFG", pribitki))

    def test_02_zastavice(self):
        # pribitki1 je hiter
        # pribitki2 zmrzne na BC zaradi bolta, potem je hiter
        # pribitki3 zmrzne na BC in CR zaradi loncev
        # pribitki4 je hitro čez BC, na CR, CD, DF ga ustavijo pešci
        self.assertEqual([7], zastavice("ABCRCRDFG", [pribitki1]))
        self.assertEqual([7], zastavice("ABCRCRDFG", [pribitki2]))
        self.assertEqual([7, 0], zastavice("ABCRCRDFG", [pribitki1, pribitki1]))
        self.assertEqual([7, 0], zastavice("ABCRCRDFG", [pribitki1, pribitki2]))
        self.assertEqual([2, 5], zastavice("ABCRCRDFG", [pribitki2, pribitki1]))
        self.assertEqual([5, 2], zastavice("ABCRCRDFG", [pribitki2, pribitki4]))
        self.assertEqual([4, 3], zastavice("ABCRCRDFG", [pribitki3, pribitki4]))
        self.assertEqual([5, 2], zastavice("ABCRCRDFG", [pribitki4, pribitki3]))
        self.assertEqual([5, 2, 0], zastavice("ABCRCRDFG", [pribitki2, pribitki4, pribitki3]))
        self.assertEqual([2, 3, 2], zastavice("ABCRCRDFG", [pribitki3, pribitki2, pribitki4]))


class Test09(unittest.TestCase):
    def test_01_cikel(self):
        try:
            zemljevid2 = zemljevid.copy()
            for p in ((O, P), (I, E)):
                del zemljevid[p]
                del zemljevid[p[::-1]]

            self.assertEqual(3, cikel("A", pribitki1))  # cikel je ABV
            self.assertEqual(3, cikel("B", pribitki1))  # cikel je BVA
            self.assertEqual(16, cikel("R", pribitki1))  # RDFGHJKMNPSTUVBC
            self.assertEqual(16, cikel("U", pribitki1))  # isti
            self.assertEqual(16, cikel("L", pribitki1))  # isti; pazi, ne vsebuje L-ja!
            self.assertEqual(16, cikel("I", pribitki1))  # isti; pazi, ne vsebuje I-ja!

            pribitki = {v: i for i, v in enumerate(sorted(pribitki1))}
            self.assertEqual(3, cikel("B", pribitki))  # cikel je BVA
            self.assertEqual(3, cikel("C", pribitki))  # isti cikel - iz C gre v B
            self.assertEqual(11, cikel("A", pribitki))  # cikel je RDFGIMNPSTU, do njega pride po ABVC
            self.assertEqual(11, cikel("V", pribitki))  # isto
            self.assertEqual(6, cikel("J", pribitki))  # JKMIGH
            self.assertEqual(6, cikel("L", pribitki))  # isto, iz L gre v JKMIGH

        finally:
            zemljevid.update(zemljevid2)


class Test10(unittest.TestCase):
    def     test_01_izpadanje(self):
        ni_pribitkov = dict.fromkeys(pribitki1, 0)
        self.assertEqual([], izpadanje(["UVB", "SPIM"], [ni_pribitkov] * 2))
        self.assertEqual([], izpadanje(["UVBCR", "SP"], [ni_pribitkov] * 2))

        # 0 izloči 1 v I
        self.assertEqual([1], izpadanje(["URIE", "TSPIG"], [ni_pribitkov] * 2))
        # 1 izloči 0 v I
        self.assertEqual([0], izpadanje(["TSPIG", "URIE"], [ni_pribitkov] * 2))
        # hkrati v I, vendar je izločen tisti z večjim indeksom
        self.assertEqual([1], izpadanje(["SPIG", "URIE"], [ni_pribitkov] * 2))
        self.assertEqual([1], izpadanje(["URIE", "SPIG"], [ni_pribitkov] * 2))

        # 2 prehiti ostala dva v I
        self.assertEqual([0, 1], izpadanje(["URIE", "SPIG", "GIM"], [ni_pribitkov] * 3))
        self.assertEqual([1, 0], izpadanje(["VURIE", "SPIG", "GIM"], [ni_pribitkov] * 3))

        # 2 ju ne prehiti, ker obstane na avtocesti
        avtocesta = ni_pribitkov.copy()
        avtocesta["avtocesta"] = 100
        self.assertEqual([0, 2], izpadanje(["VURIE", "SPI", "GIM"], [ni_pribitkov, ni_pribitkov, avtocesta]))
        self.assertEqual([0, 1, 2], izpadanje(["VURIE", "SPIG", "GIM"], [ni_pribitkov, ni_pribitkov, avtocesta]))
        self.assertEqual([1, 2, 0], izpadanje(["GIM", "SPIG", "VURIE"], [avtocesta, ni_pribitkov, ni_pribitkov]))

        # ničti izrine prvega (na P), zato prvi na izrine zadnjega, čeprav je ta na I precej pozneje
        self.assertEqual([1], izpadanje(["PNMKJ", "SPI", "GIE"], [ni_pribitkov, ni_pribitkov, avtocesta]))
        # ... isto, s premešanimi mesti
        self.assertEqual([0], izpadanje(["SPI", "PNMKJ", "GIE"], [ni_pribitkov, ni_pribitkov, avtocesta]))
        self.assertEqual([1], izpadanje(["GIE", "SPI", "PNMKJ"], [avtocesta, ni_pribitkov, ni_pribitkov]))
        self.assertEqual([2], izpadanje(["GIE", "PNMKJ", "SPI"], [avtocesta, ni_pribitkov, ni_pribitkov]))
        # ničti izrine prvega na P, drugega na I
        self.assertEqual([1, 2], izpadanje(["PNMIR", "SPI", "GIE"], [ni_pribitkov, ni_pribitkov, avtocesta]))
        # ... isto, s premešanimi mesti
        self.assertEqual([0, 2], izpadanje(["SPI", "PNMIR", "GIE"], [ni_pribitkov, ni_pribitkov, avtocesta]))
        self.assertEqual([2, 0], izpadanje(["GIE", "PNMIR", "SPI"], [avtocesta, ni_pribitkov, ni_pribitkov]))
        self.assertEqual([2, 1], izpadanje(["PNMIR", "GIE", "SPI"], [ni_pribitkov, avtocesta, ni_pribitkov]))
        self.assertEqual([2, 1], izpadanje(["SPI", "GIE", "SPI"], [ni_pribitkov, avtocesta, ni_pribitkov]))
        # ničti izrine prvega, zatem pa drugi ničtega na I (ker nima pribitka na avtocesti!)
        self.assertEqual([1, 0], izpadanje(["PNMIR", "SPI", "GIE"], [ni_pribitkov, ni_pribitkov, ni_pribitkov]))

        # vmes se še tretji ustreli v nogo
        self.assertEqual([1, 3, 0], izpadanje(["PNMIR", "SPI", "GIE", "DFD"], [ni_pribitkov] * 4))
        # ničti izrine prvega na P, drugega na I
        self.assertEqual([1, 3, 2], izpadanje(["PNMIR", "SPI", "GIE", "DFD"],
                                              [ni_pribitkov, ni_pribitkov, avtocesta, ni_pribitkov]))

        pribitki5 = dict(gravel=4, trava=1, lonci=5, bolt=0, pešci=2,
                         stopnice=4, avtocesta=1, črepinje=3, robnik=3,
                         rodeo=2)
        pribitki6 = dict(gravel=1, trava=1, lonci=2, bolt=3, pešci=1,
                         stopnice=1, avtocesta=3, črepinje=1, robnik=2,
                         rodeo=4)
        self.assertEqual([1, 3, 4, 0], izpadanje(["ABCRVUTSP", "DRCBVUT", "EI", "GHJKMNPOPS", "SPNMK"],
                                                 [pribitki1, pribitki5, pribitki1, pribitki6, pribitki1]))
        self.assertEqual([1, 4, 3, 0], izpadanje(["ABCRVUTSP", "DRCBVUT", "EI", "GHJKMNPOPS", "SPNMK"],
                                                 [pribitki5, pribitki5, pribitki6, pribitki1, pribitki1]))


if __name__ == "__main__":
    unittest.main()
