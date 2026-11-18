import pygame as pg

FPS = 60
WIN_WIDTH = 400
WIN_HEIGHT = 100
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
screen.fill(WHITE)  # белый фон
pg.display.set_caption("Игра")
clock = pg.time.Clock()
speed = 2

# до начала игрового цикла отображаем объекты:
# координаты центра круга:
c = 50
x = 0  # скрываем за левой границей
y = WIN_HEIGHT // 2 - c//2  # выравниваем по центру по вертикали
pg.draw.rect(screen, ORANGE, (x, y, c, c))
pg.display.update()  # обновляем окно

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

    # изменение состояний объектов:
    # если круг полностью скрылся за правой границей
    if x  > WIN_WIDTH - c:
        speed = -speed
        speed -= 1

    x += speed  # то на следующей итерации цикла круг отобразится немного правее

    if x < 0:
        speed = -speed
        speed += 1

    screen.fill(WHITE)  # заливаем фон, стирая предыдущий круг
    pg.draw.rect(screen, ORANGE, (x, y, c, c))

    pg.display.update()  # обновляем окно
