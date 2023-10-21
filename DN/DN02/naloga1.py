
ovire = [(1, 3, 6), (2, 4, 3), (4, 6, 7),
         (3, 4, 9), (6, 9, 5), (9, 10, 2), (9, 10, 8)]

x = int(input("x = "))
vrstica_ovire = None

i = 0
while i < len(ovire):
    zacetni_stolpec, koncni_stolpec, vrstca = ovire[i]

    if zacetni_stolpec <= x and x <= koncni_stolpec:
        if vrstica_ovire == None:
            vrstica_ovire = vrstca
        elif vrstica_ovire > vrstca:
            vrstica_ovire = vrstca 

    i += 1

print(vrstica_ovire)