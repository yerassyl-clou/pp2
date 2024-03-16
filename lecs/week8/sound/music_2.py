import pygame
pygame.mixer.init()
pygame.init()

con = True
is_blue = True
x, y = 30, 30
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

SONG_END = pygame.USEREVENT + 1

pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play()

while cond:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            cond = False
            pygame.quit()
        elif event.type == SONG_END:
            print("the song ended!")

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    
        pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]: y -= 5
    if pressed[pygame.K_DOWN]: y += 5
    if pressed[pygame.K_LEFT]: x -= 5
    if pressed[pygame.K_RIGHT]: x += 5

    screen.fill((0, 0, 0))

    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 128, 0)

    r = pygame.Rect(x, y, 60, 60)

    pygame.draw.rect(screen, color, r)

    pygame.display.flip()
    clock.tick(60)