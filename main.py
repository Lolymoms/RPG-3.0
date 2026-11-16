import pygame

pygame.init()
screen = pygame.display.set_mode((806, 806))
clock = pygame.time.Clock()
pygame.display.set_caption('Python RPG')

# test_font = pygame.font.Font('Fonts/pixel_font.otf', 100)
# text_surface = test_font.render('My Game', False, 'Black')
# text_rectangle = text_surface.get_rect(center = (640, 100))

# original_fish = pygame.image.load('Images/fish/fish_1.png').convert_alpha()
# fish = pygame.transform.scale_by(original_fish, 0.04)
# fish_rectangle = fish.get_rect(center = (45, 45))

## Put in loop !!
# pygame.display.update()
# clock.tick(60)