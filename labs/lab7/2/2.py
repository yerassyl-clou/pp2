import pygame
pygame.mixer.init()
pygame.init()

songs = [
    "labs/lab7/2/The Beach.mp3",
    "labs/lab7/2/Running.mp3",
    "labs/lab7/2/Pink + white.mp3"
]

png = pygame.image.load("labs/lab7/2/png.png")

x = 0
pygame.mixer.music.load(songs[x])

display = pygame.display.set_mode((286, 90))
pygame.display.set_caption("Music player")

run = True
while run:
    pygame.time.Clock().tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_RIGHT]:
        pygame.mixer.music.stop()
        x = x + 1
        pygame.mixer.music.load(songs[x])
        pygame.mixer.music.play()

    if pressed[pygame.K_LEFT]:
        pygame.mixer.music.stop()
        x = x - 1
        pygame.mixer.music.load(songs[x])
        pygame.mixer.music.play()
    
    if pressed[pygame.K_DOWN]:
        pygame.mixer.music.stop()
    
    if pressed[pygame.K_UP]:
        pygame.mixer.music.play()


    display.blit(png, (0, 0))
    pygame.display.flip()
    
