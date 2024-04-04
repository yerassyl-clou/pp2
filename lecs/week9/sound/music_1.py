import pygame
pygame.mixer.init()

pygame.mixer.music.load('foo.mp3')


pygame.mixer.music.play()              #play once
#pygame.mixer.music.play(-1)             play infinitly


pygame.mixer.music.queue("song_name.mp3")            #add song to queue


pygame.mixer.music.stop()                 #stop playing song


