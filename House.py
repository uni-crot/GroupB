import pygame
from pygame.draw import *
import datetime
pygame.init()

FPS = 40
w = 1100
h = 700
screen = pygame.display.set_mode((w, h))
rect(screen, (255, 255, 255), (0, 0, w, h))

print('Введите число спичек в ширину')
width = int(input())
print('Введите число спичек в длину')
length = int(input())
print('Введите число колонн с торца')
column_x = int(input())
print('Введите число колонн сбоку')
colunm_y = int(input())
match = 40

def top(screen,width,length):
    if (width <= 0) or (length <= 0):
        print('Недопустимые значения')
    else:
        rect(screen, (0, 0, 0), (50, 50, match*length, match*width),2)

top(screen,width,length)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
