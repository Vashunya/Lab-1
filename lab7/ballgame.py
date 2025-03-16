import pygame

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_radius = 25
ball_x, ball_y = screen_width // 2, screen_height // 2
step = 5

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ball_x - ball_radius - step >= 0:
        ball_x -= step
    if keys[pygame.K_RIGHT] and ball_x + ball_radius + step <= screen_width:
        ball_x += step
    if keys[pygame.K_UP] and ball_y - ball_radius - step >= 0:
        ball_y -= step
    if keys[pygame.K_DOWN] and ball_y + ball_radius + step <= screen_height:
        ball_y += step

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()