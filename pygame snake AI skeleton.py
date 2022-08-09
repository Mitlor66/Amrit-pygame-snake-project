import pygame
import time
import random

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_a,
    K_s,
    K_w,
    K_d,
    K_q,
    K_c,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_PAUSE,
    K_SPACE
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


def ai_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])


def ai_next_move(snake_head, snake_list, food_pos):
    x, y = snake_head
    fx, fy = food_pos
    if x < fx:
        if no_snake(snake_head, snake_list, ...):
            return ...snake_block, 0
    elif x > fx:
        if no_snake(snake_head, snake_list, ...):
            return ...snake_block, 0
    elif y < fy:
        if no_snake(snake_head, snake_list, ...):
            return 0, ...snake_block
    elif y > fy:
        if no_snake(snake_head, snake_list, ...):
            return 0, ...snake_block

    direction = get_free_direction(snake_head, snake_list)

    if direction == ...:
        return snake_block, 0
    elif direction == ...:
        return -snake_block, 0
    elif direction == ...:
        return 0, snake_block
    elif direction == ...:
        return 0, -snake_block
    return snake_block, 0

"""
The aim of the following function is to check whether there is a snake part in the direction the snake is currently facing
"""
def no_snake(snake_head, snake_list, direction):
    x, y = snake_head
    for pos in snake_list:
        if pos != [x, y]:
            if x-snake_block == pos[...] and direction == "left":
                return False
            if x+snake_block == pos[...] and direction == "right":
                return False
            if y+snake_block == pos[...] and direction == "down":
                return False
            if y-snake_block == pos[...] and direction == "up":
                return False
    return True

"""
The aim of the following function is to decide which position is free to go.
"""
def get_free_direction(snake_head, snake_list):
    x, y = snake_head
    directions = ["right", "left", "down", "up"]
    for d in directions:
        if d == ...:
            flag = False
            for pos in snake_list:
                if y == pos[1] and x < pos[0]:
                    flag = True
                    break
            if not flag and x < display_width-snake_block:
                return d
        if d == ...:
            flag = False
            for pos in snake_list:
                if y == pos[1] and x > pos[0]:
                    flag = True
                    break
            if not flag and x > 0:
                return d
        if d == ...:
            flag = False
            for pos in snake_list:
                if x == pos[0] and y < pos[1]:
                    flag = True
                    break
            if not flag and y < display_height-snake_block:
                return d
        if d == ...:
            flag = False
            for pos in snake_list:
                if x == pos[0] and y > pos[1]:
                    flag = True
                    break
            if not flag and y > 0:
                return d
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

    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

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

        x1_change, y1_change = ai_next_move(snake_head, snake_list, [foodx, foody])
        x1 += x1_change
        y1 += y1_change
        display.fill(blue)
        pygame.draw.rect(display, green, [foodx, foody, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        ai_snake(snake_block, snake_list)
        ai_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            while [foodx, foody] in snake_list:
                foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


while (game_loop()):
    continue
