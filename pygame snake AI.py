import pygame
import random

from pygame.locals import (
    K_q,
    K_c,
    KEYDOWN,
    QUIT,
)

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

display_width = 600
display_height = 400

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 120

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def ai_score(score):
    value = score_font.render("AI Score: " + str(score), True, yellow)
    display.blit(value, [0, 0])


def ai_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])


def ai_next_move(snake_head, snake_list, food_pos):
    x, y = snake_head
    fx, fy = food_pos
    if x < fx:
        if no_snake(snake_head, snake_list, "right"):
            return snake_block, 0
    elif x > fx:
        if no_snake(snake_head, snake_list, "left"):
            return -snake_block, 0
    elif y < fy:
        if no_snake(snake_head, snake_list, "down"):
            return 0, snake_block
    elif y > fy:
        if no_snake(snake_head, snake_list, "up"):
            return 0, -snake_block

    direction = None
    while direction is None:
        direction = get_free_direction(snake_head, snake_list)

    print(direction)
    if direction == "right":
        return snake_block, 0
    elif direction == "left":
        return -snake_block, 0
    elif direction == "down":
        return 0, snake_block
    elif direction == "up":
        return 0, -snake_block
    return snake_block, 0


def no_snake(snake_head, snake_list, direction):
    x, y = snake_head
    for pos in snake_list:
        if pos != [x, y]:
            if x-snake_block == pos[0] and direction == "left":
                return False
            if x+snake_block == pos[0] and direction == "right":
                return False
            if y+snake_block == pos[1] and direction == "down":
                return False
            if y-snake_block == pos[1] and direction == "up":
                return False
    return True


def get_free_direction(snake_head, snake_list):
    x, y = snake_head
    directions = ["right", "left", "down", "up"]
    random.shuffle(directions)
    for d in directions:
        if d == "right":
            flag = False
            for pos in snake_list:
                if y == pos[1] and x < pos[0]:
                    flag = True
                    break
            if not flag and x < display_width-snake_block:
                return "right"
        if d == "left":
            flag = False
            for pos in snake_list:
                if y == pos[1] and x > pos[0]:
                    flag = True
                    break
            if not flag and x > 0:
                return "left"
        if d == "down":
            flag = False
            for pos in snake_list:
                if x == pos[0] and y < pos[1]:
                    flag = True
                    break
            if not flag and y < display_height-snake_block:
                return "down"
        if d == "up":
            flag = False
            for pos in snake_list:
                if x == pos[0] and y > pos[1]:
                    flag = True
                    break
            if not flag and y > 0:
                return "up"
    return None


def message(msg, color):
    msg = font_style.render(msg, True, color)
    display.blit(msg, [display_width / 6, display_height / 3])


def game_loop():
    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    snake_head = [x1, y1]
    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            display.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            ai_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        return False
                    if event.key == K_c:
                        return True
                if event.type == QUIT:
                    return False

        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        x1_change, y1_change = ai_next_move(snake_head, snake_list, [food_x, food_y])
        x1 += x1_change
        y1 += y1_change
        display.fill(blue)
        pygame.draw.rect(display, green, [food_x, food_y, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        ai_snake(snake_list)
        ai_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            while [food_x, food_y] in snake_list:
                food_x = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
                food_y = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


while game_loop():
    continue
