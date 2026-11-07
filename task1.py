import pygame as pg

FPS = 60
WIDTH, HEIGHT = 1000, 600
HOUSE_SISE = 400

# цвета выбраны с сайта: https://htmlcolorcodes.com/
MINT = (181, 222, 149)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (238, 181, 50)
FIRE = (245, 112, 37)
BLUE = (7, 195, 229)
GREEN = (36, 166, 62)
BROWN = (166, 134, 36)
BROWN_1 = (189, 104, 28)
GREEN_1 = (26, 122, 54)
BLUE_1 = (135, 208, 214)
GREY = (130, 140, 143)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLUE)  # заливка фона
clock = pg.time.Clock()

# при рисовании буду опираться на длину и ширину экрана: WIDTH, HEIGHT
# рисунок: настенные часы
# циферблат
pg.draw.rect(screen,GREEN , (0,HEIGHT / 2, WIDTH, HEIGHT / 2))
pg.draw.rect(screen,BROWN , (WIDTH / 2 + 50, HEIGHT / 4, HOUSE_SISE,HOUSE_SISE))
pg.draw.rect(screen,BROWN_1 , (200,HEIGHT * 1/3, WIDTH * 1/25, HEIGHT /2))
pg.draw.circle(screen,GREEN_1 , (221, 250), 167)
pg.draw.circle(screen,BLUE_1 , (750,350 ), 140)
pg.draw.polygon(screen, GREY, [[WIDTH / 2 + 50, HEIGHT / 4], [WIDTH / 2 + 50 + HOUSE_SISE, HEIGHT / 4],[((WIDTH / 2 + 50) + (WIDTH / 2 + 50 + HOUSE_SISE)) / 2, 20],])
# отображаем нарисованные объекты
pg.display.update()

flag_play = True
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    pg.display.update()
