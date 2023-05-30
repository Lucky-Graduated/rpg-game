import pygame as pg
import sys

window_height, window_width = 600,600
display_surf = pg.display.set_mode((window_height, window_width))
pg.display.set_caption("Bhaag Milkha Bhaag!!!!")

# background
bg_surf = pg.image.load('../Assets/bg.png').convert()

# icon
icon = pg.image.load('../Assets/icon.png').convert_alpha()
pg.display.set_icon(icon)

# fps controller
clock = pg.time.Clock()

# Player
class Player(pg.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pg.image.load('../Assets/player.png').convert_alpha()
        self.rect = self.image.get_rect(center = (window_width/2, window_height/2))
        self.speed = 2

    def input_postion(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pg.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pg.K_UP]:
            self.rect.y -= self.speed

    def update(self):
        self.input_postion()

# groups
player_grp = pg.sprite.GroupSingle()

player = Player(player_grp)
# game loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    dt = clock.tick(60) / 1000
    # bg
    display_surf.blit(bg_surf,(0,0))

    # fun call
    player_grp.update()

    # blit
    player_grp.draw(display_surf)

    pg.display.update()