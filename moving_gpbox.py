import sys, pygame

# globals 
size = width, height = 320, 240
speed = [30, 100]
black = 0, 0, 0

# initialize
pygame.init()
screen = pygame.display.set_mode(size, 0, 16)

# ball
ball = pygame.image.load("firefox.png").convert()
ballrect = ball.get_rect()


# timer
start_ticks = pygame.time.get_ticks()
time_limit = 20 * 1000
clock = pygame.time.Clock()
dt = 0

# sounds
hit_floor_sound = pygame.mixer.Sound("hit_floor.wav")
hit_wall_sound = pygame.mixer.Sound("hit_wall.wav")



# generate events while key's are pressed
pygame.key.set_repeat(30, 20)

# acceleration & displacement
dvx, dvy = 5, 5
ay = 100

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE: sys.exit()
			
			if event.key == pygame.K_RIGHT:
				if ballrect.right < width:
					# ballrect = ballrect.move([dx, 0])
					# dx = dx + 1
					speed[0] = speed[0] + dvx 
			
			if event.key == pygame.K_LEFT:
				if ballrect.left > 0:
					# ballrect = ballrect.move([-dx, 0])
					speed[0] = speed[0] - dvx

			if event.key == pygame.K_UP:
				if ballrect.top > 0:
					ay += 1
			
			if event.key == pygame.K_DOWN:
				if ballrect.bottom < height:
					ay -= 1
			
	pygame.event.pump()
	
	ballrect = ballrect.move([int(v * dt/1000) for v in speed])
	
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
		hit_wall_sound.play()
		
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
		hit_floor_sound.play()
		if ballrect.top < 0:
			ballrect.top = 0
		else:
			ballrect.bottom = height
	
	# adds acceleration
	# fixme - broken. doesn't accelerate properly
	speed[1] = speed[1] + ay * int(dt/1000.0)

	screen.fill(black)
	screen.blit(ball, ballrect)
	pygame.display.update()
	
	dt = clock.tick(30) # fps
	
	# pygame.time.delay(30)
	
	# run for a limited time
	
	# if (pygame.time.get_ticks() - start_ticks) > time_limit:
	#	break

pygame.quit()


