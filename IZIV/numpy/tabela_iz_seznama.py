import numpy as np

def seznam_tabela(vrednost, visina, sirina):
    tabela = np.array(vrednost)
    tabela.resize(visina, sirina)
    return tabela

def velika_stevila(n,x):
    tabela = np.full(n,x, dtype=np.int64)
    return tabela

def odmik_od_povprecja(tabela):
    povprecje = np.mean(tabela)
    print(tabela - povprecje)

def stroski(tabela):
    vsote = np.sum(tabela, axis=0)
    print(vsote.argmax())

def enake_meritve(casi, temp1, temp2):
    enake_temperature = np.flatnonzero(temp1-temp2 == 0)
    casi = np.array(casi)
    print(casi[enake_temperature])

def brez_negativnih(tabela):
    indexi_x = np.where()
    indexi_y = [1,3]
    brez_negativnih = np.delete(tabela, indexi_x, axis=0)
    brez_negativnih = np.delete(brez_negativnih, indexi_y, axis=1)

    print(brez_negativnih)


def veckotnik(table):
    obseg = 0
    i = 0
    while i < len(table):
        dolzina = np.sqrt(np.sum((table[i-1] - table[i]) ** 2))
        obseg += dolzina
        i += 1
    print(obseg)

print("funkcija: sezna_tabel")
print(seznam_tabela([1,2,3,2,1,0], 2, 3))

print("\nfunkcija: velika_stevila")
print(sum(velika_stevila(3, 1000000000) + velika_stevila(3, 2000000000)))

print("\nfunkcija: odmik_od_povprecja")
a = np.array([[1,2,3],[4,5,6]])
odmik_od_povprecja(a)

print("\nfunkcija: stroski")
a = np.array([[1, 2, 4, 0],
             [3, 1, 1, 2],
             [0, 1, 2, 1]])
stroski(a)

print("\nfunkcija: enake_meritve")
casi = [9, 10, 12, 15, 16, 17, 18]
kraj1 = np.array([20, 22, 23, 20, 19, 21, 25])
kraj2 = np.array([20, 18, 23, 20, 22, 20, 25])
enake_meritve(casi, kraj1, kraj2)

# print("\nfunkcija: brez_negativnih")
# a = np.array([[1, 0, -3, 3, -4],
#               [1, 2, 5, 1, 8],
#               [-2, 3, 1, 4, 5],
#               [6, 2, 1, 7, 0]])


# brez_negativnih(a)

print("\nfunkcija: veckotnik")
a = np.array([[-2,1], [0,-1], [1,0], [1,2], [-1,2]])
veckotnik(a)










