import pygame
import random

pygame.init()

#Окно
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))

GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

snake_size = 10
speed = 20
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("timesnewroman", 50)
score_font = pygame.font.SysFont("comicsansms", 35)

def draw_snake(snake_size, snake_list):
    #Отрисовка змеи
    for x in snake_list:
        pygame.draw.rect(dis, BLACK, [x[0], x[1], snake_size, snake_size])

def text_end(text, color):
    #Вывод текста в конце
    mesg = font_style.render(text, True, color)
    dis.blit(mesg, [275, 290])

def show_score(score, level):
    #Показать счет и уровень
    value = score_font.render(f"Score: {score}  Level: {level}", True, PURPLE)
    dis.blit(value, [10, 10])

def generate_food(snake_list):
    #Генерация еды избегая змеи
    while True:
        foodx = round(random.randrange(0, dis_width - snake_size) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_size) / 10.0) * 10.0
        if [foodx, foody] not in snake_list:
            return foodx, foody


game_over = False
game_close = False

x = dis_width / 2
y = dis_height / 2
new_x = 0
new_y = 0

snake_list = []
snake_length = 1

foodx, foody = generate_food(snake_list)

score = 0
level = 1

while not game_over:
    #Обработка экрана с проигрышем
    while game_close:
        dis.fill(WHITE)
        text_end("GAME OVER", RED)
        show_score(score, level)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_close = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    x, y = dis_width / 2, dis_height / 2
                    new_x, new_y = 0, 0
                    snake_list = []
                    snake_length = 1
                    foodx, foody = generate_food(snake_list)
                    score = 0
                    level = 1
                    speed = 20
                    game_close = False

    #Обработка событий в игре
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and new_x != -snake_size:
                new_x = snake_size
                new_y = 0
            elif event.key == pygame.K_LEFT and new_x != snake_size:
                new_x = -snake_size
                new_y = 0
            elif event.key == pygame.K_DOWN and new_y != -snake_size:
                new_x = 0
                new_y = snake_size
            elif event.key == pygame.K_UP and new_y != snake_size:
                new_x = 0
                new_y = -snake_size

    #Проверка на столкновение со стенами
    if x >= dis_width or x < 0 or y >= dis_height or y < 0:
        game_close = True

    #Движение змеи
    x += new_x
    y += new_y

    dis.fill(WHITE)

    #Отрисовка еды
    pygame.draw.rect(dis, RED, [foodx, foody, snake_size, snake_size])

    #Обновление позиции змеи
    snake_head = [x, y]
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    #Проверка на столкновение змеи с собой
    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_close = True

    draw_snake(snake_size, snake_list)
    show_score(score, level)

    pygame.display.update()

    #Проверка на поедание еды
    if x == foodx and y == foody:
        foodx, foody = generate_food(snake_list)
        snake_length += 1
        score += 1

        #Увеличение уровня
        if score % 4 == 0:
            level += 1
            speed += 5

    #Скорость
    clock.tick(speed)

pygame.quit()