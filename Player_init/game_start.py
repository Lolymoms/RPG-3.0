import pygame
from Systems import display_systems
from Systems.game_data import screen, screen_rectangle, text_font

original_main_menu_background = pygame.image.load('Assets/Images/main_menu_background.png').convert()
main_menu_background = pygame.transform.scale(original_main_menu_background, (screen.get_size()[0] + 100, screen.get_size()[1] + 100))
main_menu_background_rectangle = main_menu_background.get_rect(center = (screen_rectangle.center))

def game_start():
    game_start_text = display_systems.split_text("Welcome adventurer! Would you like a tutorial? /n /nYes /nNo", text_font)
    if display_systems.print_selection(game_start_text, main_menu_background, main_menu_background_rectangle, True) == 'Yes':
        return ('Game start', 'Tutorial')
    else:
        return ('Game start', 'Player init')

def tutorial():
    pass

def player_initialization():
    pass