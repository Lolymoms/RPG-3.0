import pygame

# Initialization
def initialize_game():
    global screen
    global screen_rectangle
    global clock
    global text_font
    global main_menu_background
    global main_menu_background_rectangle
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen_rectangle = screen.get_rect()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Python RPG')

    # Assets
    # Font
    text_font = pygame.font.Font('Assets/Fonts/text_font.otf', 75)

    # Base background
    original_main_menu_background = pygame.image.load('Assets/Images/main_menu_background.png').convert()
    main_menu_background = pygame.transform.scale(original_main_menu_background, (screen.get_size()[0] + 100, screen.get_size()[1] + 100))
    main_menu_background_rectangle = main_menu_background.get_rect(center = (screen_rectangle.center))