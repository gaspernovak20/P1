xs = [5, 4, -7, 42, 12, -3, -4, 11, 42, 2]

videl_sem_42 = False

for stevilo in xs:
    if stevilo == 42:
        videl_sem_42 = True
        break

print(videl_sem_42)
if videl_sem_42:
    print("Res sem videl 42.")