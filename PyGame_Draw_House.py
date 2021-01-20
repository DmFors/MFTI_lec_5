import pygame
from pygame.draw import *

pygame.init()


def main():
    a, b, heading = 500, 500, 'Drawing House with PyGame'
    sc = prepare_for_drawing(a, b, heading)

    x, y, width, height = 250, 500, 250, 400
    draw_house(sc, x, y, width, height)

    fps = 30
    run_program(fps)


def prepare_for_drawing(a, b, heading):
    """
    Возвращает экран программы размером a * b
    Задаёт заголовок программы на heading
    :param a: ширина экрана
    :param b: высота экрана
    :param heading: заголовок программы
    :return: экран программы, на котором будет осуществляться рисование
    """
    sc = pygame.display.set_mode((a, b))
    pygame.display.set_caption(heading)
    sc.fill('white')
    return sc


def draw_house(sc, x, y, width, height):
    """
    Рисует дом в опорной точке (x, y).
    За опорную точку взята нижняя серединная точка фундамента.
    :param sc: экран для вывода рисунка
    :param x: расстояние от левой границы экрана программы до опорной точки
    :param y: расстояние от верхней границы экрана программы до опорной точки
    :param width: абсолютная ширина дома
    :param height: абсолютная высота дома
    :return: None
    """

    x_fnd = x
    y_fnd = y
    width_fnd = width
    height_fnd = 0.1 * height
    draw_house_foundation(sc, x_fnd, y_fnd, width_fnd, height_fnd)

    x_wall = x
    y_wall = y - height_fnd
    width_wall = 0.9 * width
    height_wall = 0.6 * height
    draw_house_walls(sc, x_wall, y_wall, width_wall, height_wall)

    draw_house_window(sc, x_wall, y_wall, width_wall, height_wall, 1)

    x_roof = x
    y_roof = y - (height_fnd + height_wall)
    width_roof = width
    height_roof = height - height_wall - height_fnd
    draw_house_roof(sc, x_roof, y_roof, width_roof, height_roof)


def draw_house_foundation(sc, x, y, width, height):
    """
    Рисует фундамент дома в опорной точке (x, y).
    За опорную точку взята нижняя серединная точка фундамента.
    :param sc: экран для вывода рисунка
    :param x: расстояние от левой границы экрана программы до опорной точки
    :param y: расстояние от верхней границы экрана программы до опорной точки
    :param width: ширина фундамента
    :param height: высота фундамента
    :return: None
    """
    start_point = convert_point(x, y, width, height)
    end_point = width, height
    color = 'grey'
    rect(sc, color, (start_point, end_point))


def draw_house_walls(sc, x, y, width, height):
    """
    Рисует стены дома в опорной точке (x, y).
    За опорную точку взята верхняя серединная точка фундамента.
    :param sc: экран для вывода рисунка
    :param x: расстояние от левой границы экрана программы до опорной точки
    :param y: расстояние от верхней границы экрана программы до опорной точки
    :param width: ширина стены
    :param height: высота стены
    :return: None
    """
    start_point = convert_point(x, y, width, height)
    end_point = width, height
    color = 'brown'
    width_wall = 1
    rect(sc, color, (start_point, end_point), width_wall)


def draw_house_window(sc, x_wall, y_wall, width_wall, height_wall, quarter):
    """
    Рисует окно дома в опорной точке (x, y).
    За опорную точку взята нижняя срединная точка одного из 4 сегментов стены дома.
    Сегменты поделены и пронумерованы по правилам четвертей декартовой системы координат.
    :param sc: экран для вывода рисунка
    :param x_wall: расстояние от левой границы экрана программы до опорной точки стены
    :param y_wall: расстояние от верхней границы экрана программы до опорной точки стены
    :param width_wall: ширина окна
    :param height_wall: высота окна
    :param quarter: четверть декартовой системы координат
    :return: None
    """
    if quarter > 2:
        y_window = y_wall
        if quarter == 3:
            x_window = x_wall - width_wall // 4
        else:
            x_window = x_wall + width_wall // 4
    else:
        y_window = y_wall - height_wall // 2
        if quarter == 2:
            x_window = x_wall - width_wall // 4
        else:
            x_window = x_wall + width_wall // 4

    n, m = 0.6, 0.8  # window proportions relative to the quarter
    width_window = n * (width_wall // 2)
    height_window = m * (height_wall // 2)

    y_window -= (1 - m) / 2 * (width_wall // 2)

    start_point = convert_point(x_window, y_window, width_window, height_window)
    end_point = width_window, height_window
    color = 'blue'
    rect(sc, color, (start_point, end_point))
    color = 'black'
    rect(sc, color, (start_point, end_point), 4)

    N = 2  # count_of_separators
    draw_house_window_frame(sc, start_point, width_window, height_window, N)


def draw_house_window_frame(sc, start_point, width, height, N):
    x_tmp, y_tmp = start_point
    dx = width / (N + 1)
    for _ in range(N):
        x_tmp += dx
        line(sc, 'black', (x_tmp, y_tmp), (x_tmp, y_tmp + height), 2)

    x_tmp, y_tmp = start_point
    dy = height / (N + 1)
    for _ in range(N):
        y_tmp += dy
        line(sc, 'black', (x_tmp, y_tmp), (x_tmp + width, y_tmp), 2)


def draw_house_roof(sc, x, y, width, height):
    """
    Рисует крышу дома в опорной точке (x, y).
    За опорную точку взята нижняя серединная точка фундамента.
    :param sc: экран для вывода рисунка
    :param x: расстояние от левой границы экрана программы до опорной точки
    :param y: расстояние от верхней границы экрана программы до опорной точки
    :param width: ширина крыши
    :param height: высота крыши
    :return: None
    """
    left_point = x - width // 2 - width % 2, y
    middle_point = x, y - height
    right_point = x + width // 2, y
    point_list = [left_point, middle_point, right_point]
    color = 'orange'
    polygon(sc, color, point_list)


def run_program(fps):
    """
    Запускает программу, окно которой обновляется fps кадров в секунду
    :param fps: количество сменяемых кадров в секунду
    :return:
    """
    pygame.display.update()
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        clock.tick(fps)


def convert_point(x, y, width, height):
    """
    Возвращает левую верхнюю точку прямоугольника по полученной опорной точке
    :param x: координата опорной точки
    :param y: координата опорной точки
    :param width: ширина прямоугольника
    :param height: высота прямоуголника
    :return: левую верхнюю точку прямоугольника
    """
    return x - width // 2 - width % 2, y - height


main()
