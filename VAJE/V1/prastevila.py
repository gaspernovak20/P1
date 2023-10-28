import time

def jePrastevilo(stevilo):
    jePrastevilo = True

    for x in range(2, int(stevilo**0.5) +1 ):
        if stevilo % x == 0:
            jePrastevilo = False
            break

    return jePrastevilo

t0 = time.time()

for stevilo in range(2, 100):
    if(jePrastevilo(stevilo)):
        print(stevilo)

t1 = time.time()

print("time:",t1-t0)