class Obstacle:
    def __init__(self, x, y, obstacle_type):
        self.x = x
        self.y = y
        self.obstacle_type = pg.image.load('./zvok-in-slika/' + obstacle_type).convert()


import pygame as pg
import random

pg.init()

# create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Slalom v d-MOL-u")

# set framerate
clock = pg.time.Clock()
FPS = 480

# player
cyclist = pg.image.load('./zvok-in-slika/kolesar.png').convert()
cyclist_width = 40
cyclist_height = 92

position_x = 0
position_y = 600 - cyclist_height

obstacle_typer = ['flowers.png', 'bottle.png', 'grass.png', 'mol.png', 'scooter.png', 'stones.png', 'walker.png']
obstacle_list = []

pg.mixer.music.load('./zvok-in-slika/arcade.mp3')
pg.mixer.music.play()

run = True

loop_counter = random.randint(30, 150)
while run:
    clock.tick(FPS)
    screen.fill((0, 0, 0))

    screen.blit(cyclist, (position_x, position_y))

    if loop_counter == 0:
        obstacle_list.append(Obstacle(random.randint(0, 800), 0, obstacle_typer[random.randint(0, 6)]))
        loop_counter = random.randint(30, 150)

    for obstacle in obstacle_list:
        if obstacle.y + 1 == SCREEN_HEIGHT:
            obstacle_list.remove(obstacle)
            continue
        obstacle.y += 1
        screen.blit(obstacle.obstacle_type, (obstacle.x, obstacle.y))

    key = pg.key.get_pressed()
    if key[pg.K_LEFT]:
        if position_x - 1 >= 0:
            position_x -= 1
    elif key[pg.K_RIGHT]:
        if position_x + 1 < (800 - cyclist_width):
            position_x += 1
    elif key[pg.K_ESCAPE]:
        run = False
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.update()
    loop_counter -= 1

pg.quit()
