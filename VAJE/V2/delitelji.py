

stevilo = int(input())

vsota_deliteljev = 0
i = 1
while i <= stevilo:
    if stevilo % i == 0:
        vsota_deliteljev += i
        print(i)
    i += 1

print("Vsota deliteljev:", vsota_deliteljev)