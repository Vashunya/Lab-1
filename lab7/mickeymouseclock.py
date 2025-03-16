import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((1400, 1000))
clock = pygame.time.Clock()

mainclock = pygame.image.load("clock.png")
seconds = pygame.image.load("sec_hand.png")  
minute = pygame.image.load("min_hand.png")
clock_center = (700, 500)

def blitrotate(surf, image, pos, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=pos)
    surf.blit(rotated_image, rotated_rect)

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = datetime.datetime.now() + datetime.timedelta(minutes=8) - datetime.timedelta(seconds=9)
    curr_seconds = current_time.second + current_time.microsecond / 1000000  
    angle_seconds = -(curr_seconds / 60) * 360  
    curr_min = current_time.minute + curr_seconds / 60  
    angle_minutes = -(curr_min / 60) * 360  

    screen.blit(mainclock, (clock_center[0] - mainclock.get_width() // 2, 
                            clock_center[1] - mainclock.get_height() // 2))

    blitrotate(screen, seconds, clock_center, angle_seconds)  
    blitrotate(screen, minute, clock_center, angle_minutes)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()