
def naj(seznam):
    return max(seznam)


def naj_abs(seznam):
    return abs(max(seznam, key=abs))


def ostevilci(xs):
    ostevilcen_seznam = []
    for i, x in enumerate(xs):
        ostevilcen_seznam.append((i, x))
    print(ostevilcen_seznam)


def bmi(oseba):
    oseba_bmi = []
    for ime, teza, visina in oseba:
        oseba_bmi.extend((ime, teza / pow(visina/100, 2)))
    print(oseba_bmi) 


def bmi2(imena, teze, visine):
    oseba_zip = zip(imena, teze, visine)
    bmi(oseba_zip)


def prastevila(meja):
    st_prastevil = 0
    for st in range(2, meja):
        for x in range(2, int(st**0.5) + 1):
            if st % x == 0:
                break
        else:
            st_prastevil += 1

    print(st_prastevil)


def palindrom(niz):
    return list(niz) == list(reversed(niz))


def palindromska_stevila():
    naj_palindrom = 0
    for x in range(1000, 99, -1):
        for y in range(x, 99, -1):
            if x*y <= naj_palindrom:
                break

            if naj_palindrom < (x*y) and palindrom(str(x*y)):
                naj_palindrom = x*y
    print(naj_palindrom)

def inverzije(xs):
    num_inverzij = 0
    for i, num in enumerate(xs):
        for i_after_num in range(i, len(xs)):
            if num > xs[i_after_num]:
                num_inverzij += 1
    print(num_inverzij)


stevila = [5, 1, -6, -7, 2]

osebe = [('Ana', 55, 165), ('Berta', 60, 153)]

imena = ['Ana', 'Berta']
teze = [55, 60]
visine = [165, 153]

print(naj(stevila))
print(naj_abs(stevila))
ostevilci([5, 1, 4, 2, 3])
bmi(osebe)
bmi2(imena, teze, visine)
prastevila(1000)
palindrom('pericarezeracirep')
palindrom('perica')
palindromska_stevila()
inverzije([1, 4, 3, 5, 2, 2, 4, 5])
