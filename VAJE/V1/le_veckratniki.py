xs = [5, 4, -7, 42, 12, -3, -4, 84, 42, 2]

videl_sem_le_veckratnike_42 = True

for stevilo in xs:
    if stevilo % 42 != 0:
        videl_sem_le_veckratnike_42 = False
        break

print(videl_sem_le_veckratnike_42)