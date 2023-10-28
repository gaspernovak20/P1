prej = [
            "..............##...",
            "..###.....###....##",
            "...###...###...#...",
            "...........#.....##",
            "...................",
            "###.....#####...###"
        ]

potem = [
            "...##..............",
            "..........###....##",
            "#..###...###...#...",
            "...###.....#.....##",
            "................###",
            "###.....##.##...###"
        ]
def dolzina_ovir(vrstica):
    st_ovir = 0
    for c in vrstica:
        if c == "#":
            st_ovir += 1

    return st_ovir 

def stevilo_ovir(vrstica):
    st_ovir = 0
    znana_ovira = False
    for c in vrstica:
        if c == "#" and not znana_ovira:
            st_ovir +=1
            znana_ovira = True
        
        if c == "." and znana_ovira:
            znana_ovira = False  

    return st_ovir

def najsirsa_ovira(vrstica):
    len_najsirse_ovira = 0
    len_ovira = 0

    znana_ovira = False
    for i in range(len(vrstica)):

        c = vrstica[i]
        # zacetek nove ovre
        if c == "#" and not znana_ovira:
            len_ovira = 1
            znana_ovira = True
            continue

        # kontrola dolzine ovire
        if c == "#" and znana_ovira:
            len_ovira += 1
        
        # konec ovire
        if (c == "." and znana_ovira) or i == (len(vrstica)-1):
            # previrimo ali je prejsnja ovira najdaljsa znana ovira do sedaj
            if len_najsirse_ovira < len_ovira:
                len_najsirse_ovira = len_ovira
            znana_ovira = False  
        
    return len_najsirse_ovira

def pretvori_vrstico(vrstica):
    seznam_parov = []
    zacetek_ovire = 0
    konec_ovire = 0

    znana_ovira = False
    for i, c in enumerate(vrstica):

        if c == "#" and not znana_ovira:
            zacetek_ovire = i+1
            znana_ovira = True
        
        if c == "." and znana_ovira:
            konec_ovire = i
            seznam_parov.append((zacetek_ovire, konec_ovire))
            znana_ovira = False

        if znana_ovira and i == len(vrstica)-1:
            konec_ovire = i+1
            seznam_parov.append((zacetek_ovire, konec_ovire))
    
    return seznam_parov

def pretvori_zemljevid(vrstice):
    seznam_ovir = []
    for i, vrstica in enumerate(vrstice):
        for ovira_kordinate in pretvori_vrstico(vrstica):
            seznam_ovir.append(ovira_kordinate+(i+1,))

    return seznam_ovir

def izboljsave(prej, potem):
    ovire_prej = pretvori_zemljevid(prej)
    ovire_potem = pretvori_zemljevid(potem)

    nove_ovire = []

    for ovira in ovire_potem:
        if ovira in ovire_prej:
            continue
        else:
            nove_ovire.append(ovira)

    return nove_ovire

def huligani(prej, potem):
    nove_ovire = izboljsave(prej, potem)

    ukradene_ovire = izboljsave(potem, prej)

    return nove_ovire, ukradene_ovire

dodane , ukradene = huligani(prej,potem)
print(dodane)
print(ukradene)
