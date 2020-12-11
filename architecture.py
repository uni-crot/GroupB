import pygame
from pygame.draw import *
import datetime
pygame.init()
FPS = 40

# константы
w = 1100
h = 700
screen = pygame.display.set_mode((w, h))
rect(screen, (255, 255, 255), (0, 0, w, h))
clock = pygame.time.Clock()

match = 40
start_x = 50
start_y = 70

finished = False
user_input = ''
count = 1

# инициализация шрифта
myfont = pygame.font.SysFont('arial', 30)
pygame.font.init()
myfont1 = pygame.font.SysFont('arial', 30)
pygame.font.init()
BLACK = (0, 0, 0)
PINK = (200, 55, 150)

# Функции
def top(screen, width, length): #рисует дом сверху
    if (number_l <= 0) or (number_w <= 0):
        return
    else:
        rect(screen, (200, 55, 150), (start_x, start_y, length, width),2)
        scoreText = myfont.render('Вид сверху', False, BLACK)
        screen.blit(scoreText, (start_x, 40))

def front(screen, width, column_x): #рисует дом с торца
    if (number_w <= 0) or (column_x < 0):
        return
    else:
        rect(screen,PINK,(4*start_x+length,start_y,width,match),2)
        for i in range(column_x+1):
            line(screen, PINK, [4*start_x+length+width*i/(column_x+1), start_y+match], [4*start_x+length+width*i/(column_x+1), start_y], 2)
        scoreText = myfont.render('Вид спереди', False, BLACK)
        screen.blit(scoreText, (4*start_x+length, 40))


def side(screen, length, column_y): #рисует дом с боковой стороны
    if (number_l <= 0) or (column_y < 0):
        return
    else:
        rect(screen, PINK, (start_x,2*start_y+width,length,match),2)
        for i in range (column_y+1):
            line(screen, PINK, [start_x+length*i/(column_y+1),2*start_y+width], [start_x+length*i/(column_y+1), 2*start_y + width+match ])
        scoreText = myfont.render('Вид с фасада', False, BLACK)
        screen.blit(scoreText, (start_x, 2*start_y+width-30))

def draw(screen, width, length, column_x, column_y):
    top(screen, width, length)
    front(screen, width, column_x)
    side(screen, length, column_y)




# рисует проекцию дома первый раз
number_l = 1
number_w = 1
column_x = 0
column_y = 0
length = number_l * match  # длина домика
width = number_w + match  # ширина домика
rect(screen, (255, 255, 255), (0, 0, w, h))
draw(screen, width, length, column_x, column_y)
pygame.display.update()

# основное тело программы
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.key == pygame.K_TAB:
                if count == 1:             number_w = int(user_input)
                    user_input = ''
                elif count == 2:
                    number_l = int(user_input)
                    user_input = ''
                elif count == 3:
                    column_x = int(user_input)
                    user_input = ''
                elif count == 4:
                    column_y = int(user_input)
                    user_input = ''
                    count = 0
                count += 1
            else:
                user_input += event.unicode
    length = number_l * match
    width = number_w * match

    # заполняет экран белым
    rect(screen, (255, 255, 255), (0, 0, w, h))

    # подписи
    scoreText = myfont.render('Чертеж здания', False, (200, 55, 150))
    screen.blit(scoreText, (40, 15))
    scoreText = myfont1.render('Авторы программы: Максимова Ксения, Корчевая Олеся', False, PINK)
    screen.blit(scoreText, (20, 670))

    # проверка на допустимые значения вводных данных
    if (number_l <= 0) or (number_w <= 0) or (column_x < 0) or (
            column_y < 0):
        scoreText = myfont.render('Недопустимое значение', False, BLACK)
        screen.blit(scoreText, (600, 450))

    # запись введеных значений в переменные (строка №87: Для подтверждения ввода значения в программе нажать клавишу TAB, у меня не получается присвоить это действие клавише ENTER)
    elif count == 1:
        scoreText = myfont.render('Введите число спичек в ширину:', False, BLACK)
        screen.blit(scoreText, (600, 450))
    elif count == 2:
        scoreText = myfont.render('Введите число спичек в длину:', False, BLACK)
        screen.blit(scoreText, (600, 450))
    elif count == 3:
        scoreText = myfont.render('Введите число колонн с торца:', False, BLACK)
        screen.blit(scoreText, (600, 450))
    elif count == 4:
        scoreText = myfont.render('Введите число колонн сбоку:', False, BLACK)
        screen.blit(scoreText, (600, 450))

    draw(screen, width, length, column_x, column_y)
    text = myfont.render(user_input, True, BLACK)
    screen.blit(text, (700, 500))

    pygame.display.flip()
    clock.tick(30)



pygame.quit()
