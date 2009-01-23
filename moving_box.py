import sys, pygame

# globals 
size = width, height = 320, 240
speed = [1, 5]
black = 0, 0, 0

# initialize
pygame.display.init()
screen = pygame.display.set_mode(size, pygame.DOUBLEBUF)
pygame.display.set_caption("Moving box!")

# ball = pygame.image.load("firefox.png").convert()

# make alpha
ball = pygame.Surface.convert_alpha(pygame.image.load("firefox.png"))


ballrect = ball.get_rect()
prev_rect = ballrect

# generate events while key's are pressed
pygame.key.set_repeat(30, 20)

dx, dy = 1, 1
ay = 2

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE: sys.exit()
			
			if event.key == pygame.K_RIGHT:
				if ballrect.right < width:
					# ballrect = ballrect.move([dx, 0])
					# dx = dx + 1
					speed[0] = speed[0] + dx
			
			if event.key == pygame.K_LEFT:
				if ballrect.left > 0:
					# ballrect = ballrect.move([-dx, 0])
					speed[0] = speed[0] - dx

			if event.key == pygame.K_UP:
				if ballrect.top > 0:
					ay += 1
			
			if event.key == pygame.K_DOWN:
				if ballrect.bottom < height:
					ay -= 1
			
			print event.key
			
	pygame.event.pump()
	
	ballrect = ballrect.move(speed)
	
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		ballrect.bottom = height
		speed[1] = -speed[1]
	
	# adds acceleration
	speed[1] = speed[1] + ay

	screen.fill(black)
	screen.blit(ball, ballrect)
	pygame.display.update()
	pygame.time.delay(30)




