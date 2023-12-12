import pygame
import time
import random
import os
import sys

width = 1000
height = 600
clock = pygame.time.Clock()
g = 1
score = 0
missed_fruits = 0
fps = 20
fruits = ['watermelon', 'orange', 'strawberry', 'banana']

pygame.init()
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Fruit Ninja Game')

background = pygame.image.load('frunin_background.jpeg')  
background = pygame.transform.scale(background, (width, height))

font = pygame.font.Font(None, 36)

def randomFruits(fruit):
    path = os.path.join(os.getcwd(), fruit+'.png')
    data[fruit] = {
        'img': pygame.image.load(path),
        'x': random.randint(100, 500),
        'y': 800,
        'speed_x': random.randint(-10, 10),
        'speed_y': random.randint(-80, -60),
        'throw': False,
        't': 0,
        'hit': False,
    }

    if random.random() >= 0.75:
        data[fruit]['throw'] = True
    else:
        data[fruit]['throw'] = False

data = {}
for fruit in fruits:
    randomFruits(fruit)

def missedFruits():
    missed_text = font.render("Missed: " + str(missed_fruits), True, (255, 0, 0))
    gameDisplay.blit(missed_text, (width - 150, 10))

pygame.display.update()

while True:
    gameDisplay.blit(background, (0, 0))  
    for key, value in data.items():
        if value['throw']:
            value['x'] = value['x'] + value['speed_x']
            value['y'] = value['y'] + value['speed_y']
            value['speed_y'] += (g*value['t'])
            value['t'] += 1

            if value['y'] <= 800:
                gameDisplay.blit(value['img'], (value['x'], value['y']))
            else:
                randomFruits(key)

            current_position = pygame.mouse.get_pos()
            if not value['hit'] and current_position[0] > value['x'] and current_position[0] < value['x']+60 and current_position[1] > value['y'] and current_position[1] < value['y']+60:
                path = os.path.join(os.getcwd(), 'half_'+key+'.png')
                value['img'] = pygame.image.load(path)
                value['speed_x'] += 10
                score += 1

                value['hit'] = True

        else:
            randomFruits(key)

    fruitScore = font.render("Score: " + str(score), True, (255, 255, 255)) 
    gameDisplay.blit(fruitScore, (10, 10))

    missedFruits()

    pygame.display.update()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
