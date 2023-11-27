xs = [5, 4, -7, 42, 12, -3, -4, 11, 42, 2]

videl_sem_veckratnik_42 = False

for stevilo in xs:
    if stevilo % 42 == 0:
        print(stevilo)
        videl_sem_veckratnik_42 = True
        break

print(videl_sem_veckratnik_42)
