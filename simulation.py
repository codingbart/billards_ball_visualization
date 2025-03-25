import pygame
import sys
import numpy as np

def run_simulation():
    pygame.init()
    WIDTH, HEIGHT = 800, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    background = pygame.image.load("bilard.svg")


    m = 1  # masa
    R = 40  # promień
    f = 0.02  # współczynnik tarcia
    g = 9.81  # przyspieszenie grawitacyjne
    x, y = 100, HEIGHT // 2  # początkowa pozycja kuli
    v = 0  # początkowa prędkość
    omega = 0  # początkowa prędkość kątowa
    h = R / 2  # wysokość przyłożenia siły 
    F = 30 # siła uderzenia

    a = F / m
    I = (2/5) * m * R**2
    alpha = (F * h) / I
    v = a * 0.1
    omega = alpha * 0.1
    theta = 0

    running = True
    while running:
        screen.blit(background, (0, 0)) 

        if v > 0:
            x += v
            v -= f * g * 0.1  # Opóźnienie przez tarcie
            omega = v / R  # Warunek toczenia

        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), R)

        dot_x = int(x + R * np.cos(theta))
        dot_y = int(y + R * np.sin(theta))
        pygame.draw.circle(screen, (255, 0, 0), (dot_x, dot_y), 3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
