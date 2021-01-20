def main():
    x, y, width, height = 100, 100, 200, 400
    draw_house(x, y, width, height)


def draw_house(x, y, width, height):
    """
    Рисует дом в опорной точке (x, y).
    За опорную точку взята нижняя серединная точка фундамента.
    :param x: Расстояние от левой границы экрана программы до опорной точки
    :param y: Расстояние от верхней границы экрана программы до опорной точки
    :param width: Абсолютная ширина дома
    :param height: Абсолютная высота дома
    :return: None
    """
    x_fnd = x
    y_fnd = y
    width_fnd = width
    height_fnd = 0.1 * height
    draw_house_foundation(x_fnd, y_fnd, width_fnd, height_fnd)

    x_wall = x
    y_wall = y + height_fnd
    width_wall = 0.9 * width
    height_wall = 0.6 * height
    draw_house_walls(x_wall, y_wall, width_wall, height_wall)

    x_roof = x
    y_roof = y_wall + height_wall
    width_roof = width
    height_roof = height - height_wall - height_fnd
    draw_house_roof(x_roof, y_roof, width_roof, height_roof)


def draw_house_foundation(x, y, width, height):
    """
    Рисует фундамент дома в опорной точке (x, y).
    За опорную точку взята нижняя серединная точка фундамента.
    :param x: Расстояние от левой границы экрана программы до опорной точки
    :param y: Расстояние от верхней границы экрана программы до опорной точки
    :param width: Ширина фундамента
    :param height: Высота фундамента
    :return: None
    """
    pass


def draw_house_walls(x, y, width, height):
    """
    Рисует стену дома в опорной точке (x, y).
    За опорную точку взята нижняя серединная точка фундамента.
    :param x: Расстояние от левой границы экрана программы до опорной точки
    :param y: Расстояние от верхней границы экрана программы до опорной точки
    :param width: Ширина стены
    :param height: Высота стены
    :return: None
    """
    pass


def draw_house_roof(x, y, width, height):
    """
    Рисует крышу дома в опорной точке (x, y).
    За опорную точку взята нижняя серединная точка фундамента.
    :param x: Расстояние от левой границы экрана программы до опорной точки
    :param y: Расстояние от верхней границы экрана программы до опорной точки
    :param width: Ширина крыши
    :param height: Высота крыши
    :return: None
    """
    pass


main()
