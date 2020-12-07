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
number_w = int(input())
print('Введите число спичек в длину')
number_l = int(input())
print('Введите число колонн с торца')
column_x = int(input())
print('Введите число колонн сбоку')
column_y = int(input())
match = 40
start_x = 50
start_y = 50
length = number_l*match #длина домика
width = number_w+match # ширина домика

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30) #инициализация шрифта

if (number_l <= 0) or (number_w <= 0) or (column_x < 0) or (column_y < 0) : #проверка на допустимые значения вводных данных
    print('Недопустимые значения')

def top(screen,width,length): #рисует дом сверху
    if (number_l <= 0) or (number_w <= 0):
        return
    else:
        rect(screen, (0, 0, 0), (start_x, start_y, length, width),2)
        scoreText = myfont.render('Вид сверху', False, (0,0,0))
        screen.blit(scoreText, (start_x, 20))

def front(screen,width,column_x): #рисует дом с торца
    if (number_w <= 0) or (column_x < 0):
        return
    else:
        rect(screen,(0,0,0),(2*start_x+length,start_y,width,match),2)
        for i in range(column_x+1):
            line(screen, (0,0,0), [2*start_x+length+width*i/(column_x+1), start_y+match],[2*start_x+length+width*i/(column_x+1),start_y],2)
        scoreText = myfont.render('Вид спереди', False, (0,0,0))
        screen.blit(scoreText, (2*start_x+length, 20))

def side(screen, length,column_y): #рисует дом с боковой стороны
    if (number_l <= 0) or (column_y < 0):
        return
    else:
        rect(screen, (0,0,0), (start_x,2*start_y+width,length,match),2)
        for i in range (column_y+1):
            line(screen, (0,0,0), [start_x+length*i/(column_y+1),2*start_y+width], [start_x+length*i/(column_y+1),2*start_y+width+match ])
        scoreText = myfont.render('Вид с фасада', False, (0,0,0))
        screen.blit(scoreText, (start_x, 2*start_y+width-30))


top(screen,width,length)
front(screen,width,column_x)
side(screen, length,column_y)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
