
stevilo = int(input())

jePrastevilo = True

for x in range(2, stevilo):
    if stevilo % x == 0:
        jePrastevilo = False
        break

if jePrastevilo:
    print(stevilo, "je prastevilo")
else:
    print(stevilo, "ni prastevilo")