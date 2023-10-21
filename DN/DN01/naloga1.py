
teza_tovora = int(input())

gorivo = 0
gorivo_natancno = 0

while teza_tovora > 0:
    teza_tovora = teza_tovora // 3 - 2
    gorivo = gorivo + 1
    # prveriti moramo da teza_tovora ni nikoli negativna 
    # kar se lahko zgodi ko je deljenje z 3 = 0 in nato ostejemo 2 -> teza_tovora = -1 
    
    # 1. nacin
    # if teza_tovora > 0:
    #     	gorivo_natancno += teza_tovora

    # 2. nacin
    gorivo_natancno += max(0, teza_tovora)

print(gorivo)
print(gorivo_natancno)
