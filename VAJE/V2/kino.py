filmi = [
    ('Poletje v skoljki 2', 6.1), 
    ('Ne cakaj na maj', 7.3), 
    ('Pod njenim oknom', 7.1),
    ('Kekec', 8.1), 
    ('Poletje v skoljki', 7.2), 
    ('To so gadi', 7.7), 
]

print("Filmi z oceno vsaj 7.0")
for film in filmi:
    naslov, ocena = film
    if ocena >= 7.0:
        print(naslov)

print("\nFilmi z najvišjo oceno:")

najboljsi_naslov = None
najboljsi_ocena = None
for film in filmi:
    naslov, ocena = film

    if najboljsi_naslov == None:
        najboljsi_naslov = naslov
        najboljsi_ocena = ocena
    elif najboljsi_ocena < ocena:
        najboljsi_naslov = naslov
        najboljsi_ocena = ocena

print(najboljsi_naslov)

print("\nPrvi film z oceno vsaj 7.0:")

for film in filmi:
    naslov, ocena = film
    if(ocena >= 7.0):
        print(naslov)
        break

print("\nPvprecna ocena vseh filmov:")

vsota_ocen = 0

for film in filmi:
    _, ocena = film
    vsota_ocen += ocena
        
print(round(vsota_ocen/len(filmi), 2))

print("\nFilmi z dvema delom:")

for film in filmi:
    naslov, _ = film
    if(naslov[-1] == "2"):
        print(naslov)