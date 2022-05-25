
"""импортируем функции из файла(модуля) logic1"""
from logic1 import *
import pygame
import sys


def d_interface(total_points, delta=0):
    """

    :param total_points: 
    :param delta:  (Default value = 0)
    font,font_1,fint_2 обращаемся к модулю pygame к его подмодулю и используем метод SysFont
    первым параметром передаём шрифт вторым его размер
    text_score, text_score_2 у шрифта вызываем метод render передаём в качестве параметров

    """
    pygame.draw.rect(screen, WHITE, TITLE_REC)
    fond = pygame.font.SysFont("stxingkai", 70)                 #шрифт, размер
    fond_2 = pygame.font.SysFont("simsun", 22)                  #шрифт, размер
    fond_3 = pygame.font.SysFont("simsun", 20)                  #шрифт, размер
    text_score = fond_2.render("Total points: ", True, BLACK)   #вызываем функцию render. параметры: текст,оптикание текста,
    text_score_2 = fond_2.render(f"{total_points}", True, BLACK)
    screen.blit(text_score, (30, 40))                           #при помощи метода blit выводим текст на экран по координатам
    screen.blit(text_score_2, (180, 40))
    if delta != 0:                                              #вывод на экран результат прибавления к счетчику
        text_delta = fond_3.render(f'+{delta}', True, BLACK)
        screen.blit(text_delta, (180, 70))
    pretty_print(mas)
    for row in range(BLOCKS):                                   #итерация по колличеству строчек(блоков)
        for column in range(BLOCKS):                            #итерация по колличеству колонок(столбиков)
            val = mas[row][column]                              #находим значения по индексам
            text = fond.render(f'{val}', True, BLACK)           #у текста вызываем метод render передаём текст, логику,цвет
            w = column * SIZ_BLOCK + (column + 1) * MAR         #находим координаты начальной точки отрисовки блока
            h = row * SIZ_BLOCK + (row + 1) * MAR + SIZ_BLOCK
            """для отрисовки передаём экран, цвет(из словаря) координаты блока, размер блока"""
            pygame.draw.rect(screen, COLOR_DISTIONARI[val], (w, h, SIZ_BLOCK, SIZ_BLOCK))
            if val != 0:
                fontw, fonth = text.get_size()                  #вызываем у текста метод get_size узнаём высоту и ширину
                if val < 9:
                    textx = w + (SIZ_BLOCK - fontw / 0.4)       #получаем координаты по горизонтали
                    texty = h + (SIZ_BLOCK - fonth / 0.6)       #вертекали
                    screen.blit(text, (textx, texty))           #передаём на экран текст и картеж с координатами
                elif 15 < val < 65:
                    textx = w + (SIZ_BLOCK - fontw / 0.65)
                    texty = h + (SIZ_BLOCK - fonth / 0.6)
                    screen.blit(text, (textx, texty))
                elif 124 < val < 999:
                    textx = w + (SIZ_BLOCK - fontw / 0.85)
                    texty = h + (SIZ_BLOCK - fonth / 0.6)
                    screen.blit(text, (textx, texty))
                elif 1024 <= val < 8222:
                    textx = w + (SIZ_BLOCK - fontw / 1)
                    texty = h + (SIZ_BLOCK - fonth / 0.6)
                    screen.blit(text, (textx, texty))



""" mas это двумерный массив который дублирует игровое поле(матрицу) """

mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

"""словарь цветов"""
COLOR_DISTIONARI = {
    0: (130, 130, 130),
    2: (255, 255, 255),
    4: (0, 255, 255),
    8: (255, 255, 0),
    16: (255, 235, 128),
    32: (255, 127, 0),
    64: (255, 255, 0),
    128: (0, 0, 255),
    256: (140, 255, 140),
    562: (160, 0, 66),
    1024: (94, 0, 94),
    2048: (255, 0, 0),
}
WHITE = (255, 255, 255)
GRAY = (130, 130, 130)
BLACK = (0, 0, 0)

"""Константные переменные:
BLOCKS колличество блоков(клеток)
SIZ_BLOCK размер блока
MAR матрица разделяющая блоки
WIDTH ширина окна
HEIGTH высота окна
TITLE_REC координаты окна счета
"""
BLOCKS = 4
SIZ_BLOCK = 110
MAR = 10
WIDTH = BLOCKS*SIZ_BLOCK + (BLOCKS+1)*MAR
HEIGTH = WIDTH+110
TITLE_REC = pygame.Rect(0, 0, WIDTH, 110)
"""счетчик посчета игровых очков"""
total_points = 0
"""кладём по индексам mas изначальные значения 2,4"""
mas[1][2] = 2
mas[3][0] = 4
mas[2][3] = 2
print(get_empty_list(mas))
"""вызываем функцию pretty_print с аргументом mas"""
pretty_print(mas)

pygame.init()#иницилизируем все компаненты
screen = pygame.display.set_mode((WIDTH, HEIGTH)) # инструкция создания экрана. принимает высоту и ширину
pygame.display.set_caption("2048")

d_interface(total_points)
pygame.display.update()

"""цикл игры"""

"""Цикл работает пока в массиве есть нули"""
while zeroo(mas) or can_move(mas):
    for event in pygame.event.get():        # обработка событий
        if event.type == pygame.QUIT:       # выход при определенных условиях(нажатие на крестик)
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:  # если тип событий нажатие кнопки
            delta = 0
            if event.key == pygame.K_LEFT:
                mas, delta = movent_left(mas)
            elif event.key == pygame.K_RIGHT:
                mas, delta = movent_right(mas)
            elif event.key == pygame.K_UP:
                mas, delta = movent_up(mas)
            elif event.key == pygame.K_DOWN:
                mas, delta = movent_down(mas)
            total_points += delta
            empty = get_empty_list(mas)         # переменная принимающая функцию get_empty_list принимающая массив
            random.shuffle(empty)               # перемешивает элементы которые не заполнены
            rannum = empty.pop()                # удаляем выбранный элемент из списка empty и передаём в переменную
            x, y = get_index_for_num(rannum)    # сохраняем в переменные координаты случайных элементов которые не заполнены
            mas = insert_2or4(mas, x, y)        # создаём массив и заполняем случаную ячейку матрицы 2 или 4
            d_interface(total_points, delta)
            pygame.display.update()             # применяем все условия к экрану
