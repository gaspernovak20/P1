
def vsota_deliteljev(stevilo):
    vsota_deliteljev = 0
    i = 1
    while i < stevilo:
        if stevilo % i == 0:
            vsota_deliteljev += i
        i += 1

    return vsota_deliteljev


stevilo = int(input())


potencjalni_prijatelj = vsota_deliteljev(stevilo)

if(stevilo == vsota_deliteljev(potencjalni_prijatelj)):
    print(potencjalni_prijatelj)
else:
    print(stevilo, "nima prijateljev.")