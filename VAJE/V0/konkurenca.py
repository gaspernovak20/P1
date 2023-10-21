
vsota = 0
stevilo_izdelkov = int(input("Število izdelkov: "))

i = 0
while i < stevilo_izdelkov:
    x = int(input("Cena artikla: "))
    vsota += x
    i += 1

print("Vsota: " , vsota)