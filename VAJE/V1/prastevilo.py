
stevilo = int(input())

jePrastevilo = True

for x in range(2, int(stevilo**0.5)+1):
    if stevilo % x == 0:
        jePrastevilo = False
        break

if jePrastevilo:
    print(stevilo, "je prastevilo")
else:
    print(stevilo, "ni prastevilo")