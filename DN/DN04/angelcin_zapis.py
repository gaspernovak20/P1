import unittest

def koordinate(obstacle):
    x1 = int(obstacle.strip('-'))
    return x1, x1 + obstacle.count('-') - 1

def vrstica(row):

    row = row.split()
    row_obstacles = []

    for obstacle in row[1:]:
        y = int(row[0][1:-1])
        row_obstacles.append(koordinate(obstacle) + (y, ))

    return row_obstacles

def preberi(map):
    map_obstacle = []

    for row in map.splitlines():
        map_obstacle += vrstica(row)

    return map_obstacle


def intervali(obstacles):
    # Simple solution
    # row_obstacles = []
    # for x, size in obstacles:
    #     row_obstacles.append(str(x) + '-' * (size - x + 1))
    # return row_obstacles

    # Advance solution
    return [f"{x}{'-' * (size - x + 1)}" for x, size in obstacles]


def zapisi_vrstico(row, row_obstacles):
    return "(" + str(row) + ") " + " ".join(intervali(row_obstacles))


def zapisi(table_obstacles):
    # Moja za kurac resitva
    # obstacles_string = ""
    # current_row = None
    #
    # for x, y, row in sorted(sorted(table_obstacles), key=lambda table_obstacles: table_obstacles[2]):
    #     if current_row != row:
    #         if obstacles_string != "":
    #             obstacles_string += "\n"
    #         current_row = row
    #         obstacles_string += "(" + str(current_row) + ")"
    #
    #     obstacles_string += " " + str(x) + '-' * (y - x + 1)
    #
    # return obstacles_string

    #Prava resitev
    rows = []
    for x, y, row in table_obstacles:
        while len(rows) <= row:
            rows.append([])
        rows[row].append((x,y))

    zemljevid = ""
    for row, obstacles in enumerate(rows):
        if obstacles:
            zemljevid += zapisi_vrstico(row, sorted(obstacles)) + "\n"

    return zemljevid

class Obvezna(unittest.TestCase):
    def test_koordinate(self):
        self.assertEqual((3, 4), koordinate("3--"))
        self.assertEqual((5, 10), koordinate("5------"))
        self.assertEqual((123, 123), koordinate("123-"))
        self.assertEqual((123, 125), koordinate("123---"))

    def test_vrstica(self):
        self.assertEqual([(1, 3, 4), (5, 11, 4), (15, 15, 4)], vrstica("  (4) 1---  5------- 15-"))
        self.assertEqual([(989, 991, 1234)], vrstica("(1234) 989---"))

    def test_preberi(self):
        self.assertEqual([(5, 6, 4),
                          (90, 100, 13), (5, 8, 13), (19, 21, 13),
                          (9, 11, 5), (19, 20, 5), (30, 34, 5),
                          (9, 11, 4),
                          (22, 25, 13), (17, 19, 13)], preberi(
""" (4) 5--
(13) 90-----------   5---- 19---
 (5) 9---           19--   30-----
(4)           9---
(13)         22---- 17---
"""))

    def test_intervali(self):
        self.assertEqual(["6-----", "12-", "20---", "98-----"], intervali([(6, 10), (12, 12), (20, 22), (98, 102)]))

    def test_zapisi_vrstico(self):
        self.assertEqual("(5) 6----- 12-", zapisi_vrstico(5, [(6, 10), (12, 12)]).rstrip("\n"))
        self.assertEqual("(8) 6----- 12- 20--- 98-----", zapisi_vrstico(8, [(6, 10), (12, 12), (20, 22), (98, 102)]).rstrip("\n"))
        self.assertEqual("(8) 6----- 12- 20--- 98-----", zapisi_vrstico(8, [(6, 10), (12, 12), (20, 22), (98, 102)]).rstrip("\n"))


class Dodatna(unittest.TestCase):
    def test_zapisi(self):
        ovire = [(5, 6, 4),
          (90, 100, 13), (5, 8, 13), (9, 11, 13),
          (9, 11, 5), (19, 20, 5), (30, 34, 5),
          (9, 11, 4),
          (22, 25, 13), (17, 19, 13)]
        kopija_ovir = ovire.copy()
        self.assertEqual("""(4) 5-- 9---
(5) 9--- 19-- 30-----
(13) 5---- 9--- 17--- 22---- 90-----------""", zapisi(ovire).rstrip("\n"))
        self.assertEqual(ovire, kopija_ovir, "Pusti seznam `ovire` pri miru")


if __name__ == "__main__":
    unittest.main()