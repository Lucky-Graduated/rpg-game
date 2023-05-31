import pygame as pg

class Player(pg.sprite.Sprite):
	def __init__(self, pos, group):
		super().__init__(group)
		self.image = pg.image.load('../Assets/player.png').convert_alpha()
		self.rect = self.image.get_rect(center = pos)

		# float based movement 
		self.pos = pg.math.Vector2(self.rect.center)
		self.direction = pg.math.Vector2()
		self.speed = 50

	def move(self,dt):

		# normalize a vector -> the length of a vector is going to be 1
		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.pos += self.direction * self.speed * dt
		self.rect.center = (round(self.pos.x), round(self.pos.y))

	def input(self):
		keys = pg.key.get_pressed()
		
		# horizontal input 
		if keys[pg.K_RIGHT]:
			self.direction.x = 1
		elif keys[pg.K_LEFT]:
			self.direction.x = -1
		else:
			self.direction.x = 0

		# vertical input
		if keys[pg.K_UP]:
			self.direction.y = -1
		else:
			self.direction.y = 0

	def gravity(self, dt):
		self.graviti = 100
		self.pos.y += self.graviti * dt

	def update(self, dt):
		self.input()
		self.move(dt)
		self.gravity(dt)