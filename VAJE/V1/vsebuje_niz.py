xs = ['foo', 'bar', 'baz', 'Waldo', 'foobar']

videl_sem_Waldo = False

for niz in xs:
    if niz == "Waldo":
        videl_sem_Waldo = True
        break

print(videl_sem_Waldo)
