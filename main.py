import pygame as pg

# -- Configurações inicais --
tm = (224, 256)
pg.init()
print('SPACE INVADERS BY PAULO')
sc = pg.display.set_mode(tm)
width, height = tm
pg.display.set_caption("Space Invaders - Paulo, 3ºC")
clock = pg.time.Clock()

# -- Carregamento dos personagens --
alien_1 = pg.image.load("Graphics/alien_1.png")
alien_2 = pg.image.load("Graphics/alien_2.png")
alien_3 = pg.image.load("Graphics/alien_3.png")
mystery = pg.image.load("Graphics/mystery.png")

# -- Configurações da nave (tamanho, posicão etc.) --
spaceship = pg.image.load("Graphics/spaceship.png")
spaceship = pg.transform.scale(spaceship, (10, 10))
spaceship_width, spaceship_height = spaceship.get_width(), spaceship.get_height()
posX_spaceship, posY_spaceship = 112, 230

# -- Variáveis globais --
gray = (29, 29, 27)
player_score = 0

# -- Loop principal --
rn = True
while rn:
    # -- 1: Tratamento do evento de saída --
    for event in pg.event.get():
        if event.type == pg.QUIT:
            rn = False

    # -- 2: Lógica de movimento (básico - mais em breve) --
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        posX_spaceship -= 1
    if keys[pg.K_RIGHT]:
        posX_spaceship += 1

    if posX_spaceship < 0:
        posX_spaceship = 0

    if posX_spaceship > width - spaceship_width:
        posX_spaceship = width - spaceship_width

    # -- 3: Renderização (ainda não terminado tudo) --
    sc.fill(gray)
    sc.blit(spaceship, (posX_spaceship, posY_spaceship))
    clock.tick(60)
    pg.display.update()

pg.quit()