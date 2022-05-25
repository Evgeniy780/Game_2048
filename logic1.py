import random


def pretty_print(mas):
    """
    функция pretty_print
    :param mas: который являеться двумерным массивом
    получаем кажлый вложенный список массива уже распакованным,
    а так же добовляем разделить между операциями *

    """
    print('*'*10)
    for row in mas:
        print(*row)
    print('*'*10)


def get_num_from_index(i, j):
    """

    :param i: индекс строки(номер)
    :param j: индекс столбца(номер)
    возвращает порядковый номер элемента +1

    """
    return i*4+j+1


def get_index_for_num(num):
    """

    :param num: порядковые номера обьектов равных нулю
    возвращает кооординаты чисел в игровой матрице(2ом массиве)

    """
    num -= 1
    x, y = num//4, num % 4
    return x, y


def insert_2or4(mas, x, y):
    """

    :param mas: 2ый массив
    :param x: номер строки
    :param y: номер столбца
    функция insert_2or4 изменяет теорию вероятности в пользу значения 2 с 75%
    и передаёт координаты свободные ячейки игровой матрица 2го массива
    возвращает 2ый массив


    """
    if random.random() <= 0.75:
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas


def get_empty_list(mas):
    """

    :param mas: двумерный массив
    проходим по всем индексам массива (строкамб, столбам)
    если по координатам индексов i, j находиться 0
    тогда передаём функцию get_num_from_index и получаем координаты равные 0
    и добовляем полученный результат в пустой список
    возвращает empty список элементов которые не заполнены указывая их порядковые номера
    при помощи функции get_num_from_index

    """
    empty = []
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                num = get_num_from_index(i, j)
                empty.append(num)
    return empty


def zeroo(mas):
    """

    :param mas: 2ый массив
    получаем из 2 мерного массива одномерный массив
    и проверяем есть ли ноль в нём
    возвращает:
        если есть True
        если нет False

    """
    for row in mas:
        if 0 in row:
            return True
    return False


def movent_left(mas):
    """

    функция movent_left перемещает все значения не ноль в левую сторону и добавляет в конец нули не более 4
    :param mas: 2ый массив
    возвращает 2ый массив и счетчик игровых очков

    """
    delta = 0
    for row in mas:         #получаем одномерный список
        while 0 in row:     #
            row.remove(0)   #убираем нули из списка
        while len(row) != 4:
            row.append(0)   #добавляем в конец одномерного списка нули до 4 значений
    for i in range(4):      #итерация по строкам и столбам
        for j in range(3):
            if mas[i][j] == mas[i][j+1] and mas[i][j] != 0:#сравниваем значения справа и если это не 0
                mas[i][j] += mas[i][j+1]                             #умножаем на 2
                delta += mas[i][j]                         #
                mas[i].pop(j+1)                            #удаляем правое одинаковое значение
                mas[i].append(0)                           #добавляем 0
    return mas, delta


def movent_right(mas):
    """

    функция movent_right перемещает все значения не ноль в правую сторону и добавляет в начало нули не более 4
    :param mas: 2ый массив
    возвращает 2ый массив и счетчик игровых очков

    """
    delta = 0
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.insert(0, 0)
    for i in range(4):
        for j in range(3, 0, -1):
            if mas[i][j] == mas[i][j-1] and mas[i][j] != 0:
                mas[i][j] += mas[i][j-1]
                delta += mas[i][j]
                mas[i].pop(j-1)
                mas[i].insert(0, 0) #insert принимает 2 значения индекс,значение
    return mas, delta


def movent_up(mas):
    """

    функция movent_up перемещает все значения не ноль вверх и добавляет внизу нули не более 4
    :param mas: 2ый массив
    возвращает 2ый массив и счетчик игровых очков

    """
    delta = 0
    for j in range(4):
        colon = []
        for i in range(4):
            if mas[i][j] != 0:
                colon.append(mas[i][j]) #всё что не ноль добавляем список
        while len(colon) != 4:          #если длина не 4, то добавляем нули
            colon.append(0)
        for i in range(3):              #
            if colon[i] == colon[i+1] and colon[i] != 0:
                colon[i] += colon[i+1]  #складываем значения
                delta += mas[i][j]
                colon.pop(i+1)
                colon.append(0)
        for i in range(4):
            mas[i][j] = colon[i]
    return mas, delta


def movent_down(mas):
    """

    функция movent_down перемещает все значения не ноль вниз и добавляет вверху нули не более 4
    :param mas: 2ый массив
    возвращает измененный 2ый массив и счетчик игровых очков

    """
    delta = 0
    for j in range(4):
        colon = []
        for i in range(4):
            if mas[i][j] != 0:
                colon.append(mas[i][j])
        while len(colon) != 4:
            colon.insert(0, 0)
        for i in range(3, 0, -1):
            if colon[i] == colon[i-1] and colon[i] != 0:
                colon[i] += colon[i-1]
                delta += mas[i][j]
                colon.pop(i-1)
                colon.insert(0, 0)
        for i in range(4):
            mas[i][j] = colon[i] #переносим горизонтальную строку в столбец массива
    return mas, delta


def can_move(mas):
    """

    :param mas: 2ый массив
    функция can_move срабатывает когда все ячейки заняты
    проводит логическое вычисление по результатам которого
    возвращает:
    True если в игровой матрице рядом находяться одинаковые значения(игра продолжаеться)
    False если в игровой матрице рядом нет одинаковых значений(игровое окно закрывается)

    """
    for i in range(3):
        for j in range(3):
            if mas[i][j] == mas[i][j+1] or mas[i][j] == mas[i+1][j]:
                return True
    return False