import pygame
from Systems.game_data import initialize_game

initialize_game()

from Systems.game_data import screen, screen_rectangle, clock, main_menu_background
from Systems.display_systems import display_background
from sys import exit
from math import sin, cos
from Player_init import game_start, load_game

# Main menu assets
# Font loading
title_text_font = pygame.font.Font('Assets/Fonts/title_font.ttf', 150)
main_menu_font = pygame.font.Font('Assets/Fonts/title_font.ttf', 100)
# Text spacing
main_menu_text_spacing = (screen_rectangle.bottom // 6)
# Title text
title_text_surface = title_text_font.render('The Great Coil', True, 'White')
title_text_rectangle = title_text_surface.get_rect(center = (screen_rectangle.centerx, (screen_rectangle.centery / 2.5)))
# Start game text
start_game_text_surface = main_menu_font.render('Start game', True, 'White')
start_game_text_rectangle = start_game_text_surface.get_rect(center = (screen_rectangle.centerx, (screen_rectangle.centery)))
# Load game text
load_game_text_surface = main_menu_font.render('Load game', True, 'White')
load_game_text_rectangle = load_game_text_surface.get_rect(center = (screen_rectangle.centerx, (screen_rectangle.centery + main_menu_text_spacing)))
# Exit text
exit_game_text_surface = main_menu_font.render('Exit game', True, 'White')
exit_game_text_rectangle = exit_game_text_surface.get_rect(center = (screen_rectangle.centerx, (screen_rectangle.centery + (main_menu_text_spacing * 2))))
# Reading box
text_reading_rectangle = pygame.Rect(0, 0, 400, 100)
text_reading_rectangle.center = (start_game_text_rectangle.center)

# Game states
def main_menu():
    main_menu_selection = 1
    main_menu_change = False
    main_menu_action = False
    while True:
        # Main event loop
        for event in pygame.event.get():
            # If the player clicks the X on a window, closes the program
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                #moves the reading box/selects the chosen action within the main menu
                if event.key == pygame.K_w:
                    main_menu_selection -= 1
                    main_menu_change = True
                elif event.key == pygame.K_s:
                    main_menu_selection += 1
                    main_menu_change = True
                elif event.key == pygame.K_RETURN:
                    main_menu_action = True
                # If the user presses escape, quits the game
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        if main_menu_change:
            main_menu_change = False
            # If the player goes further than the amount of elements, wraps around to the bottom/top
            if main_menu_selection > 3:
                main_menu_selection = 1
            elif main_menu_selection < 1:
                main_menu_selection = 3
            # Moves the reading box
            if main_menu_selection == 1:
                text_reading_rectangle.center = (start_game_text_rectangle.center)
            elif main_menu_selection == 2:
                text_reading_rectangle.center = (load_game_text_rectangle.center)
            elif main_menu_selection == 3:
                text_reading_rectangle.center = (exit_game_text_rectangle.center)
        # If the player presses enter, performs the corresponding action
        if main_menu_action:
            if main_menu_selection == 1:
                return ("Game start", "Init")
            elif main_menu_selection == 2: 
                return ("Load game", "None")
            elif main_menu_selection == 3:
                pygame.quit()
                exit()

        # Draws main menu elements
        display_background(main_menu_background, True)

        screen.blit(title_text_surface, title_text_rectangle)
        pygame.draw.rect(screen, (0, 0, 0), text_reading_rectangle)
        screen.blit(start_game_text_surface, start_game_text_rectangle)
        screen.blit(load_game_text_surface, load_game_text_rectangle)
        screen.blit(exit_game_text_surface, exit_game_text_rectangle)


        # Updates the screen and limits FPS to 60
        pygame.display.update()
        clock.tick(60)

game_state = "Main menu"
substate = 'None'

game_states = {
    'Main menu' : {
        'None' : main_menu
    },
    'Game start' : {
        'Init' : game_start.game_start,
        'Tutorial' : game_start.tutorial,
        'Player init' : game_start.player_initialization
    },
    'Load game' : {
        'None' : load_game.load_game
    }
}

while True:
    game_state, substate = game_states[game_state][substate]()