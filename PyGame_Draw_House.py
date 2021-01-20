import pygame
from pygame.draw import *


def main():
    a, b, heading = 600, 1200, 'Drawing House with PyGame'
    sc = prepare_for_drawing(a, b, heading)

    x, y, width, height = 100, 100, 200, 400
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
    y_wall = y + height_fnd
    width_wall = 0.9 * width
    height_wall = 0.6 * height
    draw_house_walls(sc, x_wall, y_wall, width_wall, height_wall)

    x_roof = x
    y_roof = y_wall + height_wall
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
    start_point = x - width // 2, y - height
    color = 'grey'


def draw_house_walls(sc, x, y, width, height):
    """
    Рисует стену дома в опорной точке (x, y).
    За опорную точку взята нижняя серединная точка фундамента.
    :param sc: экран для вывода рисунка
    :param x: расстояние от левой границы экрана программы до опорной точки
    :param y: расстояние от верхней границы экрана программы до опорной точки
    :param width: ширина стены
    :param height: высота стены
    :return: None
    """
    pass


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
    pass


def run_program(fps):
    """
    Запускает программу, окно которой обновляется fps кадров в секунду
    :param fps: количество сменяемых кадров в секунду
    :return:
    """
    pass


main()
