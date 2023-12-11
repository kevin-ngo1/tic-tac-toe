import pygame
import pygame.locals
from menu_tictactoe import menu_tictactoe_start


def choose_game():
    pygame.init()
    pygame.mixer.init()

    #Fenetre
    screen_height = 600
    screen_width = 1000
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('GamesLand')

    #Son
    pygame.mixer.music.load("music/Nintendo.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1) 

    # Variables Couleurs et Texte
    font = pygame.font.SysFont("arialblack", 70)
    sub_font= pygame.font.SysFont("arialblack", 30)
    white = "#ffffff"

    #Variables images
    background = pygame.image.load("image/sky.jpg")
    background = pygame.transform.scale(background, (screen_width, screen_height))
    kenny = pygame.image.load("image/kenny.png")
    kenny = pygame.transform.scale(kenny, (200, 200))
    kenny_rect = kenny.get_rect()
    kenny_x = 0
    kenny_y = 0
    kenny_speed = 5
    door = pygame.image.load("image/door.png")
    door = pygame.transform.scale(door, (150, 240))
    door1_rect = pygame.Rect(880, 20, 150, 200)
    door1_texte=sub_font.render("TIC TAC TOE", True, white)
    door2 = pygame.image.load("image/rick_morty.png")
    door2 = pygame.transform.scale(door2, (150, 240))
    door2_rect = pygame.Rect(880, 350,150, 200)

    #Variables
    clock=pygame.time.Clock()

    # RUN Les évènements du jeu
    run = True
    while run:

        screen.blit(background, (0, 0))
        screen.blit(kenny, (kenny_x, kenny_y))
        screen.blit(door, (800, 20))
        screen.blit(door2, (800, 350))
        screen.blit(door1_texte, (780, 0))

        kenny_rect.topleft = (kenny_x, kenny_y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and kenny_x > 0:
            kenny_x -= kenny_speed
        if keys[pygame.K_RIGHT] and kenny_x < screen_width - kenny.get_height():
            kenny_x += kenny_speed
        if keys[pygame.K_UP] and kenny_y > 0:
            kenny_y -= kenny_speed
        if keys[pygame.K_DOWN] and kenny_y < screen_height - kenny.get_height():
            kenny_y += kenny_speed

        if kenny_rect.colliderect(door1_rect):
            game_tic = menu_tictactoe_start()
            if game_tic:
                run = False
        # if kenny_rect.colliderect(door2_rect):
        #     game_over = run_tic_tac_toe()
        #     if game_over:
        #         run = False

        

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
        
