import pygame
from sys import exit

# Initialization
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_rectangle = screen.get_rect()
clock = pygame.time.Clock()
pygame.display.set_caption('Python RPG')

# Main menu 
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

# original_fish = pygame.image.load('Images/fish/fish_1.png').convert_alpha()
# fish = pygame.transform.scale_by(original_fish, 0.04)
# fish_rectangle = fish.get_rect(center = (45, 45))

game_state = "Main menu"
main_menu_selection = 1
main_menu_change = False
main_menu_action = False

# Main gameplay loop
while game_state == 'Main menu':
    for event in pygame.event.get():
        #if the user clicks the x, quits the program
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #if the user presses the space key, quits the program (placeholder)
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_w:
                main_menu_selection -= 1
                main_menu_change = True
            elif event.key == pygame.K_s:
                main_menu_selection += 1
                main_menu_change = True
            elif event.key == pygame.K_RETURN:
                main_menu_action = True
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    if main_menu_change:
        main_menu_change = False
        if main_menu_selection > 3:
            main_menu_selection = 1
        elif main_menu_selection < 1:
            main_menu_selection = 3
        if main_menu_selection == 1:
            text_reading_rectangle.center = (start_game_text_rectangle.center)
        elif main_menu_selection == 2:
            text_reading_rectangle.center = (load_game_text_rectangle.center)
        elif main_menu_selection == 3:
            text_reading_rectangle.center = (exit_game_text_rectangle.center)
    if main_menu_action:
        if main_menu_selection == 1:
            game_state = "Game start"
        elif main_menu_selection == 2: 
            game_state = "Load game"
        elif main_menu_selection == 3:
            pygame.quit()
            exit()

    # Draws main menu elements
    screen.fill((7, 4, 66))
    screen.blit(title_text_surface, title_text_rectangle)
    pygame.draw.rect(screen, (0, 0, 0), text_reading_rectangle)
    screen.blit(start_game_text_surface, start_game_text_rectangle)
    screen.blit(load_game_text_surface, load_game_text_rectangle)
    screen.blit(exit_game_text_surface, exit_game_text_rectangle)

    pygame.display.update()
    clock.tick(60)
