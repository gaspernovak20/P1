import pygame as pg
import random

Rect = pg.Rect

pg.init()

# create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Slalom v d-MOL-u")

# set frame rate
clock = pg.time.Clock()
FPS = 480

# obstacles
obstacle_typer = ['bottle.png', 'flowers.png', 'grass.png', 'mol.png', 'scooter.png', 'stones.png', 'walker.png']
obstacle_list = []

# basic
lives = 3
points = 0
level = 1


class Obstacle:
    def __init__(self, x, y, obstacle_type):
        self.type = obstacle_type
        self.obstacle_type = pg.image.load('./zvok-in-slika/' + obstacle_type)
        self.x = x
        self.y = y
        self.height = 35
        self.width = 35
        self.hit_box = (self.x, self.y, self.width, self.height)

    def move_display(self):
        self.y += 1
        self.hit_box = (self.x, self.y, self.width, self.height)
        pg.draw.rect(screen, (255, 0, 0), self.hit_box, 1)
        screen.blit(self.obstacle_type, (self.x, self.y))


class Player:
    def __init__(self):
        # player
        self.player = pg.image.load('./zvok-in-slika/kolesar.png').convert()
        self.width = 40
        self.height = 92
        self.x = SCREEN_WIDTH / 2 - self.width / 2
        self.y = 600 - self.height
        self.hit_box = (self.x, self.y, self.width, self.height)

    def display(self):
        self.hit_box = Rect(self.x, self.y, self.width, self.height)
        pg.draw.rect(screen, (255, 0, 0), self.hit_box, 1)
        screen.blit(self.player, (self.x, self.y))

    def move(self, direction):
        if direction[pg.K_LEFT]:
            if self.x - 1 >= 0:
                self.x -= 1
        elif direction[pg.K_RIGHT]:
            if self.x + 1 < (800 - self.width):
                self.x += 1


def mol_hit(mol):
    global points
    points += 1
    obstacle_list.remove(mol)
    pg.mixer.Channel(2).play(pg.mixer.Sound('./zvok-in-slika/jump.mp3'))

def obstacle_hit(hit_obstacle):
    global lives
    lives -= 1
    obstacle_list.remove(hit_obstacle)
    pg.mixer.Channel(2).play(pg.mixer.Sound('./zvok-in-slika/explosion.mp3'))


# background music
pg.mixer.music.load('./zvok-in-slika/arcade.mp3')
pg.mixer.music.play()


# player
cyclist = Player()
# text
text_font = pg.font.SysFont("Arial", 30)


def display_text(text, font, x, y):
    img = font.render(text, True, (255, 255, 255))
    screen.blit(img, (x, y))


run = True

# gostota ovir
loop_counter = random.randint(30, 160 - 10 * level)

while run:

    if lives == -1:
        pg.quit()

    if points == level * 5:
        level += 1

    # hitrost
    clock.tick(FPS + level / 10)

    screen.fill((0, 0, 0))

    cyclist.display()

    display_text(f"Tocke: {points} Stopnja: {level} Zivljenja: {lives}", text_font, 0, 0)

    # generating obstacles
    if loop_counter == 0:
        obstacle_list.append(Obstacle(random.randint(0, 800), 0, obstacle_typer[random.randint(0, 6)]))
        loop_counter = random.randint(30, 150)

    # collision detect
    for obstacle in obstacle_list:
        if cyclist.hit_box.colliderect(obstacle.hit_box):
            if obstacle.type == "mol.png":
                mol_hit(obstacle)
            else:
                obstacle_hit(obstacle)
        break

    # cleaning obstacles
    for obstacle in obstacle_list:
        if obstacle.y + 1 == SCREEN_HEIGHT:
            obstacle_list.remove(obstacle)
            continue
        obstacle.move_display()

    # key detection
    key = pg.key.get_pressed()

    # cyclist movement
    cyclist.move(key)

    # other options
    if key[pg.K_ESCAPE]:
        run = False
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.update()
    loop_counter -= 1

pg.quit()
