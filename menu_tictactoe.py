import pygame
from pygame.locals import *
import os
from tictactoe import run_tic_tac_toe

def menu_tictactoe_start():
    pygame.init()

    #Fenetre
    screen_height = 600
    screen_width = 1100
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Future Tic Tac Toe')
    background = pygame.image.load("image/tictactoemenu.jpg")
    background = pygame.transform.scale(background, (screen_width, screen_height))

    #Variables

    white="#ffffff"
    blue="#3b97d4"
    red="#f70a0a"
    font_mario = os.path.join("font", "MarioWorldPixelColor.ttf")
    button_text_font = pygame.font.Font(None, 90)
    title_font = pygame.font.Font(font_mario, 70)
    title_text=title_font.render("TIC TAC TOE", True, blue)
    p1_button = pygame.Rect(screen_width//2 - 165, screen_height //2 - 50, 300, 60)
    p1_text = button_text_font.render('1 JOUEUR', True, red)
    p2_button = pygame.Rect(screen_width//2 - 180, screen_height //2 + 100, 350, 60)
    p2_text = button_text_font.render('2 JOUEURS', True, red)
    level_button_easy= pygame.Rect(screen_width//2 - 100, screen_height //2 - 100, 170, 60)
    level_text_easy= button_text_font.render('EASY', True, red)
    level_button_hard= pygame.Rect(screen_width//2 - 100, screen_height //2 + 50, 180, 60)
    level_text_hard= button_text_font.render('HARD', True, red)

    def difficulty_options():
        pygame.draw.rect(screen, (0,0,0,0), level_button_easy, 0)
        pygame.draw.rect(screen, (0,0,0,0), level_button_hard, 0)
        screen.blit(background, (0, 0))
        screen.blit(level_text_easy, (screen_width // 2 - 100,screen_height //2 - 100))      
        screen.blit(level_text_hard, (screen_width // 2 - 100,screen_height //2 + 50))

    def menu():
        pygame.draw.rect(screen, (0,0,0,0), p2_button,0) 
        pygame.draw.rect(screen, (0,0,0,0), p1_button,0) 
        screen.blit(background, (0, 0))
        screen.blit(p1_text, (screen_width // 2 - 170,screen_height //2 - 50))      
        screen.blit(p2_text, (screen_width // 2 - 180,screen_height //2 + 100))
        screen.blit(title_text, (165,30))

    show_menu = True

    #Run Les évènements et jeu
    run = True
    while run:

        if show_menu :
            menu()
        else :
            difficulty_options()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if p2_button.collidepoint(event.pos):
                    mode_jeu = 2
                    game_tic_2 = run_tic_tac_toe(mode_jeu)
                    if game_tic_2:
                        run = False
                if p1_button.collidepoint(event.pos):
                    show_menu = False
                if level_button_easy.collidepoint(event.pos):
                    mode_jeu=1
                    run_tic_tac_toe(mode_jeu)
                    run = False
                if level_button_hard.collidepoint(event.pos):
                    mode_jeu=3
                    run_tic_tac_toe(mode_jeu)
                    run = False

        pygame.display.update()

    pygame.quit()