import pygame
import sys
from simulation import run_simulation

pygame.init()
WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load("billiards_background.jpg") 
title_font = pygame.font.Font(None, 50)
button_font = pygame.font.Font(None, 40)

def start_screen():
    while True:
        screen.blit(background, (0, 0))
        title_text = title_font.render("Ruch kuli bilardowej", True, (255, 255, 255))
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))

        start_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 30, 200, 60)
        button_text = button_font.render("START SYMULACJI", True, (0, 0, 0))
        screen.blit(button_text, (WIDTH // 2 - button_text.get_width() // 2, HEIGHT // 2 - 20))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(event.pos):
                run_simulation()  

start_screen()
