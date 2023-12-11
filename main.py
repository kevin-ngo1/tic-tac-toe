import pygame
from pygame.locals import *
from choose import choose_game
import os

pygame.init()

# Fenetre
screen_height = 500
screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('GamesLand')

# Variables

#Couleurs et font
font = pygame.font.SysFont("arialblack", 70)
font_pixel = os.path.join("font", "pixel.ttf")
sub_font= pygame.font.SysFont("arialblack", 50)
black = "#000000"
grey="#4f4a4a"

#Mise en place
background = pygame.image.load("image/base.jpg")
background = pygame.transform.scale(background, (screen_width, screen_height))
button_text_font = pygame.font.Font(font_pixel, 55)
button_text2_font = pygame.font.Font(font_pixel, 60)
play_rect = pygame.Rect(screen_width // 2 - 300, screen_height // 2-40, 300, 60)
play_text = button_text2_font.render("Start", True, grey)
exit_rect = pygame.Rect(screen_width // 2 + 100, screen_height // 2 -40 , 215, 70)
exit_text = button_text_font.render("Exit", True, grey)
title_font = pygame.font.Font(font_pixel, 70)
title_text=title_font.render("GAMELANDS", True, black)

# Couleurs
blue = "#236794"
white = "#ffffff"
pink="#961b4e"

    

# RUN Les évènements du jeu
run = True
while run:

    pygame.draw.rect(screen, pink, play_rect)
    pygame.draw.rect(screen, pink, exit_rect)
    screen.blit(background, (0, 0))
    screen.blit(title_text, (92,30))
    screen.blit(play_text, (screen_width // 2 - 300, screen_height // 2 - 40))
    screen.blit(exit_text, (screen_width // 2 + 100, screen_height //2 -40))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if exit_rect.collidepoint(event.pos):
                run = False
            elif play_rect.collidepoint(event.pos):
                game_over = choose_game()
                if game_over:
                    run = False

    pygame.display.update()

pygame.quit()
