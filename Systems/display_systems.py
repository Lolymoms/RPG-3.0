import pygame
from math import sin, cos
from Systems import game_data

def split_text(text, font = game_data.text_font):
    words = text.split()
    current_text = ''
    text_to_print = []
    for word in words:
        # If the newline character is in the string, makes a new line
        if '/n' in word:
            if len(current_text) != 0:
                seperation = (font.get_linesize() * len(text_to_print))
                text_to_print.append((current_text, seperation, font, False))
            seperation = (font.get_linesize() * len(text_to_print))
            new_word = word.removeprefix("/n")
            # If the /n is just to make a space, doesn't make it a selectable option
            if len(new_word) == 0:
                text_to_print.append((new_word, seperation, font, False))
            else:
                text_to_print.append((new_word, seperation, font, True))
            current_text = ''
            continue
        # If there's no words in the string, just measures the length of one word
        elif len(current_text) == 0:
            text_size = font.size(word)[0]
        # Otherwise it measures the length of the string, a space, and a new word
        else:
            text_size = font.size(current_text + ' ' + word)[0]

        # If the length of the measured string and new word is more than the width of the screen, add the old string to a list, and the new word to a blank string
        if text_size > (game_data.screen_rectangle.width - 20):
            seperation = (font.get_linesize() * len(text_to_print))
            text_to_print.append((current_text, seperation, font, False))
            current_text = word
        # Otherwise it permanently adds the word to the string
        else:
            if len(current_text) != 0:
                current_text += ' '
            current_text += word

    seperation = (font.get_linesize() * len(text_to_print))
    text_to_print.append((current_text, seperation, font, False))
    current_text = ''

    return text_to_print

# Input should be text_to_print, or some other list with sentences already measured with spacing
def print_text(text):
    for sentence, separation, font, selection in text:
        text_printing = font.render(sentence, True, 'White')
        text_printing_rectangle = text_printing.get_rect(topleft = (10, separation))
        game_data.screen.blit(text_printing, text_printing_rectangle)

# Input should be the same as print_text()
def print_selection(text, background, background_rect, move_background = False):
    current_selection = 0
    player_selection = 1
    chosen_selection = False
    total_selections = 0
    for tuple in text:
        if tuple[3]:
            total_selections += 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                elif event.key == pygame.K_w:
                    player_selection -= 1
                elif event.key == pygame.K_s:
                    player_selection += 1
                elif event.key == pygame.K_RETURN:
                    chosen_selection = True

        # Draws the background. Moves it if selected
        if move_background:
            offset_x = (sin(pygame.time.get_ticks() / 1400) * 50)
            offset_y = (cos(pygame.time.get_ticks() / 1300) * 50)
            background_rect.centerx = (game_data.screen_rectangle.centerx + offset_x)
            background_rect.centery = (game_data.screen_rectangle.centery + offset_y)
        game_data.screen.blit(background, background_rect)

        # If the player presses w or s too much, wraps around
        if player_selection <= 0:
            player_selection = total_selections
        elif player_selection > total_selections:
            player_selection = 1

        if current_selection == total_selections:
            current_selection = 0

        for sentence, separation, font, selection in text:
            if selection:
                current_selection += 1
            text_printing = font.render(sentence, True, 'White')
            text_printing_rectangle = text_printing.get_rect(topleft = (10, separation))
            if current_selection == player_selection:
                pygame.draw.rect(game_data.screen, (0, 0, 0), text_printing_rectangle)
                if chosen_selection:
                    return sentence
            game_data.screen.blit(text_printing, text_printing_rectangle)

        # Updates the screen and limits FPS to 60
        pygame.display.update()
        game_data.clock.tick(60)

def display_background(background, move_background = False):
    background_rectangle = background.get_rect(center = (game_data.screen_rectangle.center))
    if move_background:
        # Moves the background slightly if selected
        offset_x = (sin(pygame.time.get_ticks() / 1400) * 50)
        offset_y = (cos(pygame.time.get_ticks() / 1300) * 50)
        background_rectangle.centerx = (game_data.screen_rectangle.centerx + offset_x)
        background_rectangle.centery = (game_data.screen_rectangle.centery + offset_y)
        
    game_data.screen.blit(background, background_rectangle)