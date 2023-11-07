def seznam_tabela(vrednost, visina, sirina):
    tabela = np.array(vrednost)
    tabela.resize(visina, sirina)
    return tabela

def velika_stevila(n,x):
    tabela = np.full(n,x, dtype=np.int64)
    return tabela

def odmik_od_povprecja(tabela):
    povprecje = np.mean(tabela)
    return tabela - povprecje

def stroski(tabela):
    vsote = np.sum(tabela, axis=0)
    return vsote.argmax()

def enake_meritve(casi, temp1, temp2):
    enake_temperature = np.flatnonzero(temp1-temp2 == 0)
    casi = np.array(casi)
    return casi[enake_temperature]

def brez_negativnih(tabela):
    indexi_x = []
    indexi_y = []

    for i, row in enumerate(tabela):
        indexi_x.extend(np.where(row < 0)[0])

    for i, collumn in enumerate(tabela.T):
        indexi_y.extend(np.where(collumn < 0)[0])

    brez_negativnih = np.delete(tabela, indexi_y, axis=0)
    brez_negativnih = np.delete(brez_negativnih, indexi_x, axis=1)

    return brez_negativnih


def veckotnik(table):
    obseg = 0
    i = 0
    while i < len(table):
        dolzina = np.sqrt(np.sum((table[i-1] - table[i]) ** 2))
        obseg += dolzina
        i += 1
    return obseg


### ^^^ Naloge rešujte nad tem komentarjem. ^^^ ###

import unittest
import numpy as np


class TestVaje(unittest.TestCase):
    def test_seznam_tabela(self):
        self.assertTrue(np.array_equal(seznam_tabela([2,5,6,7,1,0], 3, 2), np.array([[2,5],[6,7],[1,0]])))
        self.assertTrue(np.array_equal(seznam_tabela([1], 1, 1), np.array([[1]])))

    def test_velika_stevila(self):
        a = velika_stevila(3, 1000000000)
        b = velika_stevila(3, 2000000000)
        c = a + b
        self.assertTrue(np.array_equal(c, np.array([3000000000, 3000000000, 3000000000])))

        a = velika_stevila(1, 8888888888888888880)
        b = velika_stevila(1, 8888888888888888881)
        self.assertNotEqual(a[0], b[0])

    def test_odmik(self):
        a = np.array([[1,2,3,4,5,6]])
        self.assertTrue(np.array_equal(odmik_od_povprecja(a), np.array([[-2.5,-1.5,-0.5,0.5,1.5,2.5]])))
        b = np.array([[1,3], [0,4]])
        self.assertTrue(np.array_equal(odmik_od_povprecja(b), np.array([[-1, 1], [-2, 2]])))

    def stroski(self):
        a = np.array([1, 2, 4, 0],
                     [3, 1, 1, 2],
                     [0, 1, 2, 1])
        self.assertEqual(stroski(a), 2)
        a = np.array([1, 2, 4, 6],
                     [3, 7, 1, 3])
        self.assertEqual(stroski(a), 1)

    def test_enake_meritve(self):
        casi = [9, 10, 12, 15, 16, 17, 18]
        kraj1 = np.array([20, 22, 23, 20, 19, 21, 25])
        kraj2 = np.array([20, 18, 23, 20, 22, 20, 25])
        self.assertTrue(np.array_equal(enake_meritve(casi, kraj1, kraj2), np.array([9,12,15,18])))

    def test_brez_negativnih(self):
        a = np.array([[1, 0, -3, 3, -4],
                      [1, 2, 5, 1, 8],
                      [-2, 3, 1, 4, 5],
                      [6, 2, 1, 7, 0]])
        self.assertTrue(np.array_equal(brez_negativnih(a), np.array([[2,1],[2,7]])))
        a = np.array([[1,2,3],[4,-5,6],[7,8,9]])
        self.assertTrue(np.array_equal(brez_negativnih(a), np.array([[1,3],[7,9]])))

    def test_veckotnik(self):
        a = np.array([[-2,1], [0,-1], [1,0], [1,2], [-1,2]])
        self.assertAlmostEqual(veckotnik(a), 4+4*2**0.5)

if __name__ == '__main__':
    unittest.main(verbosity=2)
