


vsota = 0

cena_artikla = 1
st_artiklov = 0

while cena_artikla != 0 and st_artiklov < 10 and vsota < 100 :
    cena_artikla = int(input("Cena artikla: "))
    if cena_artikla == 0:
        break
    st_artiklov = st_artiklov + 1
    vsota += cena_artikla
    

print("Porabili boste " , vsota , " evrov za " , st_artiklov , " stvari.")