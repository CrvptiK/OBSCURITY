import pygame
from screen.window import OverlayWindow

overlay = OverlayWindow(1920, 1080)

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    overlay.clear()

    pygame.draw.circle(
        overlay.screen,
        (0, 255, 0),
        (500, 500),
        50
    )

    overlay.update()

    clock.tick(60)

pygame.quit()