import pygame
from Systems.game_data import main_menu_background, clock
from Systems.display_systems import display_background, split_text, print_text

def load_game():
    unavailable_text = split_text("This feature currently doesn't exist! Please start a new game. Press escape to return to the main menu.")
    print(unavailable_text)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return ('Main menu', 'None')
                
        display_background(main_menu_background, True)
        print_text(unavailable_text)

        pygame.display.update()
        clock.tick(60)