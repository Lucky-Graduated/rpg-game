import pygame as pg
import sys
from player import Player

window_height, window_width = 1280, 720
display_surf = pg.display.set_mode((window_height, window_width))
pg.display.set_caption("Bhaag Milkha Bhaag!!!!")
# fps controller
clock = pg.time.Clock()

# background
bg = pg.image.load('../Assets/background.png').convert()
ground = pg.image.load('../Assets/ground.png').convert_alpha()

# icon
icon = pg.image.load('../Assets/icon.png').convert_alpha()
pg.display.set_icon(icon)


all_sprites = pg.sprite.Group()
player = Player((window_height/2, window_width/2), all_sprites)

# game loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    dt = clock.tick(60) / 1000

    all_sprites.update(dt)
    display_surf.blit(bg, (0,0))
    display_surf.blit(ground, (window_height-300, window_width-168))

    all_sprites.draw(display_surf)

    pg.display.update()