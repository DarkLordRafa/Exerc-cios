import pygame
pygame.init()

w = 300;
h = 300
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Bauhaus')
TPImage = pygame.image.load('bau.jpg').convert()
x = 100;
y = 300;
screen.blit(TPImage, (x, y))
pygame.display.flip()
running = True
pygame.mixer.music.load('bauhaus.mp3')
pygame.mixer.music.play()
while(running):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			