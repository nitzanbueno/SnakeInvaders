import pygame
import copy
from random import randint
import random
import itertools
import ctypes
MessageBox = ctypes.windll.user32.MessageBoxA
pygame.init()

size = int(raw_input("Size?"))
pixelsize = int(raw_input("Pixel Size?"))

w=pixelsize*size
h=pixelsize*size

surface = pygame.display.set_mode((w,h))


black = pygame.transform.scale(pygame.image.load("black_box.png"),(pixelsize,pixelsize))
white = pygame.transform.scale(pygame.image.load("white_box.png"),(w,h))
red = pygame.transform.scale(pygame.image.load("red_box.png"),(pixelsize,pixelsize))
blue = pygame.transform.scale(pygame.image.load("blue_box.png"),(pixelsize,pixelsize))
turquoise = pygame.transform.scale(pygame.image.load("turquoise_box.png"),(pixelsize,pixelsize))
bigturq = pygame.transform.scale(pygame.image.load("turquoise_box.png"),(w,h))
green = pygame.transform.scale(pygame.image.load("green_box.png"),(pixelsize,pixelsize))
dark_green = pygame.transform.scale(pygame.image.load("dark_green_box.png"),(pixelsize,pixelsize))
yellow = pygame.transform.scale(pygame.image.load("yellow_box.png"),(pixelsize,pixelsize))
purple = pygame.transform.scale(pygame.image.load("purple_box.png"),(pixelsize,pixelsize))

alien_up = pygame.transform.scale(pygame.image.load("alien_up.png"),(pixelsize,pixelsize))
alien_down = pygame.transform.scale(pygame.image.load("alien_down.png"),(pixelsize,pixelsize))

bullet_up = pygame.transform.scale(pygame.image.load("bullet_0_-1.png"),(pixelsize,pixelsize))
bullet_down = pygame.transform.scale(pygame.image.load("bullet_0_1.png"),(pixelsize,pixelsize))
bullet_left = pygame.transform.scale(pygame.image.load("bullet_-1_0.png"),(pixelsize,pixelsize))
bullet_right = pygame.transform.scale(pygame.image.load("bullet_1_0.png"),(pixelsize,pixelsize))

snake_up_left = pygame.transform.scale(pygame.image.load("snake_up_left.png"),(pixelsize,pixelsize))
snake_up_right = pygame.transform.scale(pygame.image.load("snake_up_right.png"),(pixelsize,pixelsize))
snake_down_left = pygame.transform.scale(pygame.image.load("snake_down_left.png"),(pixelsize,pixelsize))
snake_down_right = pygame.transform.scale(pygame.image.load("snake_down_right.png"),(pixelsize,pixelsize))
snake_vert = pygame.transform.scale(pygame.image.load("snake_vert.png"),(pixelsize,pixelsize))
snake_hori = pygame.transform.scale(pygame.image.load("snake_hori.png"),(pixelsize,pixelsize))

snake_dr_hd = pygame.transform.scale(pygame.image.load("snake_down_right_head_down.png"),(pixelsize,pixelsize))
snake_dr_hr = pygame.transform.scale(pygame.image.load("snake_down_right_head_right.png"),(pixelsize,pixelsize))
snake_dr_td = pygame.transform.scale(pygame.image.load("snake_down_right_tail_down.png"),(pixelsize,pixelsize))
snake_dr_tr = pygame.transform.scale(pygame.image.load("snake_down_right_tail_right.png"),(pixelsize,pixelsize))
snake_ur_hu = pygame.transform.scale(pygame.image.load("snake_up_right_head_up.png"),(pixelsize,pixelsize))
snake_ur_hr = pygame.transform.scale(pygame.image.load("snake_up_right_head_right.png"),(pixelsize,pixelsize))
snake_ur_tu = pygame.transform.scale(pygame.image.load("snake_up_right_tail_up.png"),(pixelsize,pixelsize))
snake_ur_tr = pygame.transform.scale(pygame.image.load("snake_up_right_tail_right.png"),(pixelsize,pixelsize))
snake_dl_hd = pygame.transform.scale(pygame.image.load("snake_down_left_head_down.png"),(pixelsize,pixelsize))
snake_dl_hl = pygame.transform.scale(pygame.image.load("snake_down_left_head_left.png"),(pixelsize,pixelsize))
snake_dl_td = pygame.transform.scale(pygame.image.load("snake_down_left_tail_down.png"),(pixelsize,pixelsize))
snake_dl_tl = pygame.transform.scale(pygame.image.load("snake_down_left_tail_left.png"),(pixelsize,pixelsize))
snake_ul_hu = pygame.transform.scale(pygame.image.load("snake_up_left_head_up.png"),(pixelsize,pixelsize))
snake_ul_hl = pygame.transform.scale(pygame.image.load("snake_up_left_head_left.png"),(pixelsize,pixelsize))
snake_ul_tu = pygame.transform.scale(pygame.image.load("snake_up_left_tail_up.png"),(pixelsize,pixelsize))
snake_ul_tl = pygame.transform.scale(pygame.image.load("snake_up_left_tail_left.png"),(pixelsize,pixelsize))
snake_hd = pygame.transform.scale(pygame.image.load("snake_down_head.png"),(pixelsize,pixelsize))
snake_td = pygame.transform.scale(pygame.image.load("snake_down_tail.png"),(pixelsize,pixelsize))
snake_hu = pygame.transform.scale(pygame.image.load("snake_up_head.png"),(pixelsize,pixelsize))
snake_tu = pygame.transform.scale(pygame.image.load("snake_up_tail.png"),(pixelsize,pixelsize))
snake_hr = pygame.transform.scale(pygame.image.load("snake_right_head.png"),(pixelsize,pixelsize))
snake_tr = pygame.transform.scale(pygame.image.load("snake_right_tail.png"),(pixelsize,pixelsize))
snake_hl = pygame.transform.scale(pygame.image.load("snake_left_head.png"),(pixelsize,pixelsize))
snake_tl = pygame.transform.scale(pygame.image.load("snake_left_tail.png"),(pixelsize,pixelsize))

class Firearm:
	is_enemy_bullet = False
	hitalien = False

	# def __init__(self, x, y, power, ai, dx, dy, speed, radius):
	# 	self.x = x
	# 	self.y = y
	# 	self.power = power
	# 	self.ai = ai
	# 	self.dx = dx
	# 	self.dy = dy
	# 	self.speed = speed
	# 	self.radius = radius


	def __init__(self, cell, power, ai, speed, radius):
		self.x = cell.x
		self.y = cell.y
		self.power = power
		self.ai = ai
		self.dx = cell.dx
		self.dy = cell.dy
		self.speed = speed
		self.radius = radius

	def hits(self, alien):
		r = self.radius
		if r > 0:
			return self.y - r <= alien.y and self.y + r >= alien.y and self.x - r <= alien.x and self.x + r >= alien.x
		else:
			return int(self.x) == int(alien.x) and int(self.y) == int(alien.y)
		# if self.ai > 1:
		# 		if self.dx == 0:
		# 			if self.dy == 1:
		# 				pinned = pinned and self.y >= alien.y
		# 			else:
		# 				pinned = pinned and self.y <= alien.y
		# 		elif self.dy == 0:
		# 			if self.dx == 1:
		# 				pinned = pinned and self.x >= alien.x
		# 			else:
		# 				pinned = pinned and self.x <= alien.x
		#return pinned

	def hit(self, alien):
		global aliens
		global snake
		t = alien.toughness
		if alien.ai <= self.ai:
			if self.ai == 7 and (alien.ai == 1 or boss != None):
				snake.hunger += 10
			alien.toughness -= self.power
			self.power -= t
			self.hitalien = True
		else:
			alien.toughness = t
			if self.dx == 0:
				alien.x = (self.x - self.radius - 1) % size
			else:
				alien.y = (self.y - self.radius - 1) % size
		if alien.toughness <= 0:
			try:
				aliens.remove(alien)
				self.x = alien.x
				self.y = alien.y
			except:
				pass

	def move(self):
		self.x = self.x + self.dx * self.speed
		self.y = self.y + self.dy * self.speed

class Alien:
	color = pygame.Color(0,0,255)
	is_boss = False

	def __init__(self, x, y, speed, ai, toughness):
		self.x = x
		self.y = y
		self.speed = speed
		self.ai = ai
		self.toughness = toughness

	def move(self):
		self.x -= self.speed

	def hits(self, cell):
		return (self.x <= cell.x and self.x + 1 >= cell.x) and self.y == cell.y
	def launch(self, speed, toughness, ai, radius, shotfirearms):
		f = Firearm(Cell(self.x, self.y,-1,0), toughness, ai, speed, radius)
		f.is_enemy_bullet = True
		shotfirearms.append(f)
		return shotfirearms

class Cell:
	x = 0
	y = 0
	dx = 0
	dy = 1
	def __init__(self, x, y, dx, dy):
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy

class Food:
	def __init__(self, x, y, saturation):
		self.x = x
		self.y = y
		self.saturation = saturation

class Snake:
	initcell = Cell(0,0,0,1)
	direction = (0,1)
	cells = [Cell(0,0,0,1)]
	hunger = 0
	lives = 5
	deflectime = 0

	def __init__(self, initcell):
		self.initcell = initcell
		hunger = 0
		lives = 5
	def move_snake(self, food):
		if len(self.cells) + self.hunger <= 0:
			reset("you were too short to do something in the game")
			return self.eat()
		newfood = food
		success = ""
		if self.deflectime > 0:
			self.deflectime -= 1
		lc = self.lastcell()
		nx = (lc.x + lc.dx) % (size / 2)
		ny = (lc.y + lc.dy) % size
		grown = False
		for cell in self.cells:
			if lc.x == cell.x and lc.y == cell.y and lc != cell:
				reset("you hit yourself")
				return self.eat()
		if nx == food.x and ny == food.y:
			self.hunger += food.saturation
			newfood = self.eat()
		if self.hunger > 0:
			self.cells.append(Cell(nx,ny,self.lastcell().dx,self.lastcell().dy))
			self.hunger -= 1
		elif self.hunger < 0 and len(self.cells) > 1:
			self.cells.pop(0)
			self.hunger += 1
		elif self.hunger < 0:
			self.hunger = 0
		else:
			for cell in self.cells:
				cell.x += cell.dx
				cell.y += cell.dy
				cell.x %= (size / 2)
				cell.y %= size
			newcells = copy.deepcopy(self.cells)
			for x in range(len(self.cells) - 1, 0, -1):
				if self.cells[x].dx != self.cells[x-1].dx or self.cells[x].dy != self.cells[x-1].dy:
					newcells[x-1].dx = self.cells[x].dx
					newcells[x-1].dy = self.cells[x].dy
			self.cells = copy.deepcopy(newcells)
		return newfood
	def lastcell(self):
		return self.cells[len(self.cells) - 1]
	def eat(self):
		allspots = []
		for spot in itertools.product(range(size/2),range(size)):
			allspots.append(spot)
		for cell in self.cells:
			try:
				allspots.remove((cell.x,cell.y))
			except:
				pass
		foodloc = allspots[randint(0,len(allspots)-1)]
		return Food(foodloc[0], foodloc[1], 2)
	def launch(self, shotfirearms, speed, toughness, ai, radius, hunger):
		fa = list(shotfirearms)
		if len(self.cells) - hunger <= 0:
			return fa
		self.hunger -= hunger
		fa.append(Firearm(self.lastcell(), toughness, ai, speed, radius))
		return fa



def spawn_alien(times):
	global seconds
	global aliens
	possiblealiens = [[1,0.5,5,pygame.Color(0,0,255)]]
	if seconds > 10:
		possiblealiens.append([1,1,5,pygame.Color(0,0,255)])
	if seconds > 20:
		possiblealiens.append([2,0.5,5,pygame.Color(0,255,0)])
		possiblealiens.append([3,0.5,5,pygame.Color(0,255,0)])
		possiblealiens.append([3,0.5,5,pygame.Color(0,255,0)])
		possiblealiens.append([4,0.5,5,pygame.Color(0,255,0)])
	if seconds > 30:
		possiblealiens.append([5,0.5,5,pygame.Color(255,0,255)])
		possiblealiens.append([4,0.25, 50, pygame.Color(255,255,0)])
	for i in range(times):
		a = random.choice(possiblealiens)
		alien = Alien(size, randint(0,size), a[1], a[0], a[2])
		alien.color = a[3]
		aliens.append(alien)

def getpic(bullet, r, g, b):
	pic = bullet_up
	if bullet.dx == -1:
		pic = bullet_left
	elif bullet.dx == 1:
		pic = bullet_right
	elif bullet.dy == 1:
		pic = bullet_down
	for x in range(pixelsize):
		for y in range(pixelsize):
			if pic.get_at((x,y)).a == 255:
				pic.set_at((x,y), pygame.Color(r,g,b,255))
	return pic

def colorize(pic, color):
	npic = copy.copy(pic)
	npic.fill(color, special_flags = pygame.BLEND_ADD)
	return npic

firearms = []
enemy_firearms = []
aliens = []
seconds = 0
numofaliens = 0
boss = None
is_up = True

def update_physics(millisecs, movealiens):
	global firearms
	global enemy_firearms
	global aliens
	global boss
	global is_up
	global snake
	is_up = (millisecs % 500) < 250
	is_shoot_time = (millisecs % 500) <= 10
	for bullet in firearms:
		bullet.move()
		if bullet.ai == 6:
			bullet.x = bullet.x % size
			bullet.y = bullet.y % size
		if bullet.x >= size + bullet.speed or bullet.y >= size + bullet.speed or bullet.x < 0 or bullet.y < 0 or bullet.power <= 0:
			if bullet.ai == 7 and not bullet.hitalien:
				snake.hunger -= 5
			firearms.remove(bullet)
	for bullet in enemy_firearms:
		bullet.move()
		if ((bullet.x >= size or bullet.y >= size or bullet.x < 0 + bullet.speed or bullet.y < 0 + bullet.speed) and bullet.ai < 4) or bullet.power <= 0:
			enemy_firearms.remove(bullet)

	if len(firearms) > 0 and len(enemy_firearms) > 0:
		for goodb in firearms:
			for badb in enemy_firearms:
				if goodb.hits(badb):
					p = copy.deepcopy(goodb.power)
					goodb.power -= badb.power
					badb.power -= p
				if goodb.power <= 0:
					try:
						firearms.remove(goodb)
					except:
						pass
				if badb.power <= 0:
					enemy_firearms.remove(badb)
	for alien in aliens:
		if is_shoot_time and alien.ai > 4:
			enemy_firearms = alien.launch((alien.ai - 3) / 2, 4, alien.ai - 4, 0, enemy_firearms)
		alai = alien.ai
		if movealiens:
			alien.move()
		if alien.x < 0:
			snake.lives -= 1
			aliens.remove(alien)
		if snake.lives < 1:
			reset("5 aliens crossed your side of the board")
			return
		for cell in snake.cells:
			for bullet in enemy_firearms:
				if bullet.hits(cell):
					if snake.deflectime > 0:
						enemy_firearms.remove(bullet)
						bullet.dx = 1
						bullet.dy = 0
						bullet.ai = 5
						bullet.power = 5
						firearms.append(bullet)
						snake.hunger += 1
					else:
						reset("an alien's bullet hit you")
					return
			if alien.hits(cell):
				if not alien.hits(snake.lastcell()):
					if snake.deflectime == 0:
						reset("an alien hit you")
						return
					else:
						aliens.remove(alien)
						snake.hunger -= 3
				else:
					if alien.ai < 2 or boss != None:
						try:
							aliens.remove(alien)
							snake.hunger += 10
						except:
							pass
					else:
						reset("an alien hit you")
						return
		for bullet in firearms:
			if bullet.hits(alien):
				bullet.hit(alien)
	#Boss Alien
	if boss != None:
		for bullet in firearms:
			if bullet.hits(boss):
				bullet.hit(boss)
		if boss.toughness <= 0:
			boss = None	
snake = []

food = []

def reset(reason):
	global snake
	global food
	global firearms
	global enemy_firearms
	global aliens
	global seconds
	global freezetime
	global boss
	global running
	global numofaliens
	if reason != "":
		if boss != None:
			reason = "You were bossed out"
		ses = "s"
		if numofaliens == 1:
			ses = ""
		result = MessageBox(None, "You survived for %(aliens)s alien%(s)s until %(reason)s.\nDo you want to play again?" % {"aliens" : numofaliens, "s" : ses, "reason" : reason}, "Game over", 4)
		if result == 6:
			balls = []
			newballs = []
			millisecs = 0
		else:
			running = False
	boss = None
	seconds = 0
	numofaliens = 0
	snake = Snake(Cell(0,0,1,0))
	snake.hunger = 6
	snake.cells = [Cell(0,0,1,0),Cell(1,0,1,0),Cell(2,0,1,0),Cell(3,0,1,0)]
	snake.deflectime = 0
	food = snake.eat()
	firearms = []
	enemy_firearms = []
	aliens = []
	freezetime = 0

reset("")

running = True
processing = False
framing = False
millisecs = 0
prevmillisecs = 0
pausing = False
fast = 0
freezetime = 0

prevdx = 1
prevdy = 0

while running:
	millisecs = millisecs % 4000
	prevmillisecs = prevmillisecs % 4000
	if not pausing:
		food = snake.move_snake(food)
		update_physics(millisecs, freezetime == 0)
		if freezetime > 0:
			freezetime -= 1
		else:
			freezetime = 0
		for i in range(fast):
			food = snake.move_snake(food)
	if millisecs % 1000 < prevmillisecs % 1000 and not pausing:
		seconds += 1
		if boss == None:
			numofaliens += 1
			spawn_alien(1)
		if seconds % 70 == 0 and seconds != 0:
			numofaliens += 1
			boss = Alien(size - 3, size / 2, 0, 5, 300)
			boss.color = pygame.Color(0,0,0)
		if boss != None:
			spawn_alien(3)
			numofaliens += 5

	key_pressed = False
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			lc = snake.lastcell()
			is_small = len(snake.cells) == 1
			if key_pressed:
				pass
			elif event.key == pygame.K_RIGHT and (lc.dx != -1 or lc.dy != 0 or is_small):
				lc.dx = 1
				lc.dy = 0
				key_pressed = True
			elif event.key == pygame.K_LEFT and (lc.dx != 1 or lc.dy != 0 or is_small):
				lc.dx = -1
				lc.dy = 0
				key_pressed = True
			elif event.key == pygame.K_DOWN and (lc.dx != 0 or lc.dy != -1 or is_small):
				lc.dx = 0
				lc.dy = 1
				key_pressed = True
			elif event.key == pygame.K_UP and (lc.dx != 0 or lc.dy != 1 or is_small):
				lc.dx = 0
				lc.dy = -1
				key_pressed = True
			elif event.key == pygame.K_p:
				pausing = not pausing
			elif event.key == pygame.K_f and len(snake.cells) + snake.hunger > 5:
				snake.deflectime += 50
				snake.hunger -= 5
			elif event.key == pygame.K_s:
				fast -= 10
			elif event.key == pygame.K_d:
				fast = 0
			elif event.key == pygame.K_q:
			 	firearms = snake.launch(firearms, 2, 5, 2, 2, 1)
			elif event.key == pygame.K_w:
			 	firearms = snake.launch(firearms, 5, 5, 3, 3, 2)
			elif event.key == pygame.K_e:
				firearms = snake.launch(firearms, 2, 24, 6, 4, 10)
			elif event.key == pygame.K_r:
				firearms = snake.launch(firearms, 2, 5, 5, 2, 2)
			elif event.key == pygame.K_z:
				firearms = snake.launch(firearms, 2, 5, 7, 3, 5)
			elif event.key == pygame.K_SPACE and boss != None:
				firearms = snake.launch(firearms, 5, 50, 4, 10, 15)
			elif event.key == pygame.K_t and len(snake.cells) + snake.hunger > 5:
				freezetime += 50
				snake.hunger -= 5
			elif event.key == pygame.K_y and boss == None:
				snake.hunger += 10
				spawn_alien(5)
				numofaliens += 5
			elif event.key == pygame.K_a and len(snake.cells) + snake.hunger > 10:
				try:
					aliens.pop(0)
					snake.hunger -= 10
				except:
					print "No Aliens"
			elif event.key == pygame.K_RETURN:
				reset("")

	# Display
	if freezetime == 0:
		surface.blit(white,(0,0))
	else:
		surface.blit(bigturq,(0,0))
	for x in range(len(snake.cells)-1):
		pic = snake_hori
		dx = snake.cells[x].dx
		dy = snake.cells[x].dy
		nx = snake.cells[x+1].dx
		ny = snake.cells[x+1].dy

		if x == len(snake.cells) - 2:
			pic = snake_hl
			if dx == 0 and nx == 0:
				if dy == 1:
					pic = snake_hu
				else:
					pic = snake_hd
			elif dx == 1 and ny == 1:
				pic = snake_dl_hd
			elif dy == -1 and nx == -1:
				pic = snake_dl_hl
			elif dx == -1 and ny == -1:
				pic = snake_ur_hu
			elif dy == 1 and nx == 1:
				pic = snake_ur_hr
			elif dx == -1 and ny == 1:
				pic = snake_dr_hd
			elif dy == -1 and nx == 1:
				pic = snake_dr_hr
			elif dx == 1 and ny == -1:
				pic = snake_ul_hu
			elif dy == 1 and nx == -1:
				pic = snake_ul_hl
			elif dx == -1:
				pic = snake_hr
		else:
			if dx == 0 and nx == 0:
				pic = snake_vert
			elif (dx == 1 and ny == 1) or (dy == -1 and nx == -1):
				pic = snake_down_left
			elif (dx == -1 and ny == -1) or (dy == 1 and nx == 1):
				pic = snake_up_right
			elif (dx == -1 and ny == 1) or (dy == -1 and nx == 1):
				pic = snake_down_right
			elif (dx == 1 and ny == -1) or (dy == 1 and nx == -1):
				pic = snake_up_left

		if snake.deflectime > 0 and freezetime == 0:
			pic = colorize(pic, pygame.Color(0,255,255))
		elif snake.deflectime > 0 and freezetime > 0:
			pic = colorize(pic, pygame.Color(0,0,255))
		surface.blit(pic, (snake.cells[x+1].x * pixelsize,snake.cells[x+1].y * pixelsize))
	dx = prevdx
	dy = prevdy
	nx = snake.cells[0].dx
	ny = snake.cells[0].dy

	pic = snake_tr
	if dx == 0 and nx == 0:
		if dy == 1:
			pic = snake_td
		else:
			pic = snake_tu
	elif dx == 1 and ny == 1:
		pic = snake_dl_tl
	elif dy == -1 and nx == -1:
		pic = snake_dl_td
	elif dx == -1 and ny == -1:
		pic = snake_ur_tr
	elif dy == 1 and nx == 1:
		pic = snake_ur_tu
	elif dx == -1 and ny == 1:
		pic = snake_dr_tr
	elif dy == -1 and nx == 1:
		pic = snake_dr_td
	elif dx == 1 and ny == -1:
		pic = snake_ul_tl
	elif dy == 1 and nx == -1:
		pic = snake_ul_tu
	elif dx == -1:
		pic = snake_tl

	if snake.deflectime > 0:
			pic = colorize(pic, pygame.Color(0,255,255))
			if freezetime > 0:
				pic = colorize(pic, pygame.Color(0,0,255))
	surface.blit(pic, (snake.cells[0].x * pixelsize,snake.cells[0].y * pixelsize))

	for firearm in firearms:
		aipic = getpic(firearm, 255, 0, 0)
		if firearm.ai > 2:
			aipic = getpic(firearm, 0, 100, 0)
		surface.blit(aipic, (firearm.x * pixelsize,firearm.y * pixelsize))

	for firearm in enemy_firearms:
		aipic = getpic(firearm, 0, 255, 255)
		if freezetime > 0:
			aipic = getpic(firearm, 0, 0, 255)
		surface.blit(aipic, (firearm.x * pixelsize,firearm.y * pixelsize))
	for alien in aliens:
		aipic = colorize(alien_down, alien.color)
		if is_up:
			aipic = colorize(alien_up, alien.color)
		surface.blit(aipic, (alien.x * pixelsize,alien.y * pixelsize))
	if boss != None:
		surface.blit(boss.aipic, (boss.x * pixelsize,boss.y * pixelsize))
	surface.blit(black, (food.x * pixelsize,food.y * pixelsize))
	if fast <= 0:
		pygame.time.delay(20 - fast)
		prevmillisecs = millisecs
		if freezetime == 0:
			millisecs += 20 - fast
	prevdx = nx
	prevdy = ny
	pygame.display.update()