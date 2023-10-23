filmi = ['Poletje v skoljki 2', 'Ne cakaj na maj', 'Pod njenim oknom', 'Kekec', 'Poletje v skoljki', 'To so gadi']
ocene = [6.1, 7.3, 7.1, 8.1, 7.2, 7.7]

for i in range(len(filmi)):
    stevilo_presledkov = 0
    for char in filmi[i]:
        if char == " ":
            stevilo_presledkov += 1
    if stevilo_presledkov == 2:
        print(filmi[i], ocene[i])



