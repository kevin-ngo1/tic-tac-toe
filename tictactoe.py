import pygame
from pygame.locals import *
import random
from ia import ia_difficile, ia_facile

def run_tic_tac_toe(mode_jeu):
    global score_player1, score_player2, game_over, clicked,player,pos,list,winner

    pygame.init()

    #Fenetre
    screen_height = 440
    screen_width = 390
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Future Tic Tac Toe')

    #Couleurs
    red = "#8f1209"
    green = "#0bba48"
    blue = "#247da6"
    yellow = "#e8f007"
    cyan= "#0cad98"
    black="#000000"


    font = pygame.font.SysFont(None, 40)

    #Variables
    line_width = 6
    clicked = False
    player = 1
    pos = (0,0)
    list = []
    game_over = False
    winner = 0
    score_player1 = 0
    score_player2 = 0


    restart_rect = Rect(screen_width // 2 - 80, screen_height // 2, 160, 50)


    for x in range (3):
        row = [0] * 3
        list.append(row)

    #Fonctions
    
    #La grille
    def draw_board():
        color = "#ffffff"
        grid = "#3f94b5"
        screen.fill(color)
        for x in range(1, 3):
            pygame.draw.line(screen, grid, (0, 130 * x + 50), (screen_width, 130 * x + 50), line_width)
            pygame.draw.line(screen, grid, (130 * x, 50), (130 * x, screen_height + 50), line_width)

    #Croix et Rond
    def draw_list():
        x_pos = 0
        for x in list:
            y_pos = 0
            for y in x:
                if y == 1:
                    pygame.draw.line(screen, red, (x_pos * 130 + 20, y_pos * 130 + 70), (x_pos * 130 + 110, y_pos * 130 + 160), line_width)
                    pygame.draw.line(screen, red, (x_pos * 130 + 110, y_pos * 130 + 70), (x_pos * 130 + 20, y_pos * 130 + 160), line_width)
                if y == -1:
                    pygame.draw.circle(screen, green, (x_pos * 130 + 65, y_pos * 130 + 115), 50, line_width)
                y_pos += 1
            x_pos += 1	

    #Comment peut terminer la partie
    def check_game_over():
        global game_over
        global winner
        global score_player1
        global score_player2

        x_pos = 0
        for x in list:
            if sum(x) == 3:
                winner = 1
                game_over = True
            if sum(x) == -3:
                winner = 2
                game_over = True
            if list[0][x_pos] + list [1][x_pos] + list [2][x_pos] == 3:
                winner = 1
                game_over = True
            if list[0][x_pos] + list [1][x_pos] + list [2][x_pos] == -3:
                winner = 2
                game_over = True
            x_pos += 1

        if list[0][0] + list[1][1] + list [2][2] == 3 or list[2][0] + list[1][1] + list [0][2] == 3:
            winner = 1
            game_over = True
        if list[0][0] + list[1][1] + list [2][2] == -3 or list[2][0] + list[1][1] + list [0][2] == -3:
            winner = 2
            game_over = True

        if game_over == False:
            tie = True
            for row in list:
                for i in row:
                    if i == 0:
                        tie = False
            if tie == True:
                game_over = True
                winner = 0

        if game_over:		
            if winner == 1:
                score_player1 += 1
            elif winner == 2:
                score_player2 += 1

    #Fin Recommencer la partie
    def draw_game_over(winner):
        if winner != 0:
            win_text = "Le joueur " + str(winner) + " a gagné !"
        elif winner == 0:
            win_text = "Egalité"

        win_img = font.render(win_text, True, yellow)
        win_rect = win_img.get_rect(center=(screen_width // 2, screen_height // 2))
        pygame.draw.rect(screen, cyan, win_rect) 
        screen.blit(win_img, win_rect)

        restart_text = 'RESTART'
        restart_img = font.render(restart_text, True, yellow)
        restart_rect = restart_img.get_rect(center=(screen_width // 2, screen_height // 2 + 35))
        pygame.draw.rect(screen, cyan, restart_rect) 
        screen.blit(restart_img, restart_rect)

    #RUN Les évènements pygame et le jeu
    run = True
    while run:

        draw_board()
        draw_list()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if mode_jeu==2:
                if game_over == False:
                    if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                        clicked = True
                    if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                        clicked = False
                        pos = pygame.mouse.get_pos()
                        cell_x = pos[0] // 130
                        cell_y = (pos[1] - 50) // 130
                        if list[cell_x][cell_y] == 0:
                            list[cell_x][cell_y] = player
                            player *= -1
                            check_game_over()
            if mode_jeu==1:
                if game_over == False:
                    if player == 1:
                        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                            clicked = True
                        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                            clicked = False
                            pos = pygame.mouse.get_pos()
                            cell_x = pos[0] // 130
                            cell_y = (pos[1] - 50) // 130
                            if list[cell_x][cell_y] == 0:
                                list[cell_x][cell_y] = player
                                player *= -1
                                check_game_over()
                    elif player == -1:
                        move = ia_facile(list, -1)
                        if move is not False:
                            row = move // 3
                            col = move % 3
                            if list[row][col] == 0:
                                list[row][col] = -1
                                player = 1
                                check_game_over()
            if mode_jeu==3:
                if game_over == False:
                    if player == 1:
                        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                            clicked = True
                        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                            clicked = False
                            pos = pygame.mouse.get_pos()
                            cell_x = pos[0] // 130
                            cell_y = (pos[1] - 50) // 130
                            if list[cell_x][cell_y] == 0:
                                list[cell_x][cell_y] = player
                                player *= -1
                                check_game_over()
                    elif player == -1:
                        move = ia_difficile(list, -1)
                        if move is not False:
                            row = move // 3
                            col = move % 3
                            if list[row][col] == 0:
                                list[row][col] = -1
                                player = 1
                                check_game_over()


        if game_over == True:
            draw_game_over(winner)
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                if restart_rect.collidepoint(pos):
                    game_over = False
                    player = 1
                    pos = (0,0)
                    list = []
                    winner = 0
                    for x in range (3):
                        row = [0] * 3
                        list.append(row)
                        
        score_text = f"Joueur 1: {score_player1}  Joueur 2: {score_player2}"
        score_img = font.render(score_text, True, black)
        screen.blit(score_img, (10, 10))
        pygame.display.update()


    pygame.quit()
    return True

        


