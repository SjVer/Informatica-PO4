import pygame as pg
from math import ceil
from time import sleep
from random import randint

DISPLAY_SIZE = (300, 300)
GRID_SIZE = 10

SLEEP_TIME = 0.25

LINE_COLOR = (255, 255, 255)
PLAYER_COLOR = (0, 255, 0)
APPLE_COLOR = (255, 0, 0)

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class Game:
	def __init__(self, host):
		""" maak een nieuwe Game instance """
		self.host = host
		self.DISPLAY = None
		self.is_running: bool = False
		self.score = 0

		self.direction: int = 0
		# up = 0
		# right = 1
		# down = 2
		# left = 3
		self.player_body: list = []
		self.apple_pos = (0,0)

	def run(self):
		"""start de game"""
		pg.init()
		
		self.player_body.append((int(GRID_SIZE/2), int(GRID_SIZE/2)))
		self.new_apple()
		self.direction = 0

		self.is_running = True
		self.DISPLAY = pg.display.set_mode(DISPLAY_SIZE)
		
		while self.is_running:
			self.handle_events()
			self.move_player()
			self.check_stuff()
			self.draw_display()
			pg.display.flip()
			sleep(SLEEP_TIME)
		
		self.quit()

	def new_apple(self):
		new_pos = (randint(0, GRID_SIZE - 1), randint(0, GRID_SIZE - 1))
		while new_pos == self.apple_pos or new_pos in self.player_body:
			new_pos = (randint(0, GRID_SIZE - 1), randint(0, GRID_SIZE - 1))
		self.apple_pos = new_pos

	def quit(self):
		"""stop de game"""
		self.DISPLAY = None
		print(f"Final Score: {self.score}")
		sleep(3)
		pg.quit()

	def handle_events(self):
		for event in pg.event.get():

			if event.type == pg.QUIT:
				self.is_running = False

			elif event.type == pg.KEYDOWN:
				if (event.key == pg.K_DOWN or event.key == pg.K_s) and self.direction != UP:
					self.direction = DOWN
				elif (event.key == pg.K_RIGHT or event.key == pg.K_d) and self.direction != LEFT:
					self.direction = RIGHT
				elif (event.key == pg.K_LEFT or event.key == pg.K_a) and self.direction != RIGHT:
					self.direction = LEFT
				elif (event.key == pg.K_UP or event.key == pg.K_w) and self.direction != DOWN:
					self.direction = UP


	def move_player(self):
		# player_body: [staart, ..., hoofd]
		
		old_x = self.player_body[-1][0]
		old_y = self.player_body[-1][1]

		if self.direction == UP:
			self.player_body.append((old_x, old_y - 1))
		if self.direction == RIGHT:
			self.player_body.append((old_x + 1, old_y))
		if self.direction == DOWN:
			self.player_body.append((old_x, old_y + 1))
		if self.direction == LEFT:
			self.player_body.append((old_x - 1, old_y))

		self.player_body.pop(0) # delete oude staart

	def check_stuff(self):
		head_pos = self.player_body[-1]

		# check of de player zichzelf raakt
		for block in self.player_body[:-1]:
			if block == head_pos:
				self.is_running = False
				print("\nGame Over: You hit yourself!")

		# check of de player tegen een muur botst
		if head_pos[0] >= GRID_SIZE or head_pos[1] >= GRID_SIZE:
			self.is_running = False
			print("\nGame Over: You hit a wall!")
		elif head_pos[0] < 0 or head_pos[1] < 0:
			self.is_running = False
			print("\nGame Over: You hit a wall!")

		# check if de player de appel raakt
		if self.apple_pos == head_pos:
			self.score += 1
			self.player_body.append(head_pos)
			self.new_apple()


	def draw_display(self):
		self.DISPLAY.fill((0,0,0))

		window_width = pg.display.get_surface().get_width()
		window_height = pg.display.get_surface().get_height()

		width = window_width / GRID_SIZE
		height = window_height / GRID_SIZE

		# player
		for block in self.player_body:
			pg.draw.rect(self.DISPLAY, PLAYER_COLOR, 
				pg.Rect(block[0] * width, block[1] * height, width, height))

		# apple
		pg.draw.rect(self.DISPLAY, APPLE_COLOR,
			pg.Rect(self.apple_pos[0] * width, 
					self.apple_pos[1] * height,
					width, height))

		# grid
		rows = window_height / height
		cols = window_width / width

		for x in range(ceil(cols)):
			pos1 = (x * width, 0)
			pos2 = (x * width, window_height)
			pg.draw.line(self.DISPLAY, LINE_COLOR, pos1, pos2)

		for y in range(ceil(rows)):
			pos1 = (0, y * height)
			pos2 = (window_width, y * height)
			pg.draw.line(self.DISPLAY, LINE_COLOR, pos1, pos2)

    
    