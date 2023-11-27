
stevilo = int(input())

vsota_deliteljev = 0
i = 1
while i < stevilo:
    if stevilo % i == 0:
        vsota_deliteljev += i
    i += 1

if stevilo == vsota_deliteljev:
    print("Podano stevilo JE POPOLNO")
else:
    print("Podano stevilo NI POPOLNO")
