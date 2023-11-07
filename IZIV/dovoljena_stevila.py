import numpy as np

not_allawed = np.array([
    (12, 18),
    (2, 5),
    (3, 8),
    (0, 4),
    (15, 19),
    (6, 9),
    (13, 17),
    (4, 8)
])

max_num = np.max(not_allawed)

first_allowed = max_num + 1
num_allowed = 0

i = 0
while i < max_num:
    for min, max in not_allawed:
        if min <= i <= max:
            print(i, "je vsebovan v", (min, max))
            break
    else:
        if first_allowed == max_num + 1:
            first_allowed = i
        num_allowed += 1
        print(i, "je dovoljeno")
    i += 1

print("Stevilo dovoljenih:", num_allowed)
print("Prvo dovoljeno:", first_allowed)
