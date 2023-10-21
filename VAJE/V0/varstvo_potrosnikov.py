
vsota = 0

x = int(input("Cena artikla: "))
st_izdelkov = 0
while x != 0:
    vsota += x
    x = int(input("Cena artikla: "))
    st_izdelkov = st_izdelkov+1

print("Vsota: " , vsota)
print("Povprecna cena: ", vsota/st_izdelkov)