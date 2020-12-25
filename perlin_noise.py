import random
import math


def perlin_noise(x, y, grid):
    #print('поиск в точке - ' + str(x) + ' ' + str(y))
    x = x / 100
    y = y / 100
    #print('x y поделени на 100 - ' + str(x) + ' ' + str(y))

    x_sect = int(x)
    y_sect = int(y)
    #print('найдени кординати сектора - ' + str(x_sect) + ' ' + str(y_sect))

    x_loc = x - x_sect
    y_loc = y - y_sect
    #print('найдени локольние кординати - ' + str(x_loc) + ' ' + str(y_loc))

    top_left_gradient = grid[x_sect][y_sect]
    top_right_gradient = grid[x_sect + 1][y_sect]
    bottom_left_gradient = grid[x_sect][y_sect + 1]
    bottom_right_gradient = grid[x_sect + 1][y_sect + 1]
    #print('найдени градиенти - ' + str(top_left_gradient) + ' ' + str(top_right_gradient) + ' ' + str(bottom_left_gradient) + ' ' + str(bottom_right_gradient))

    vector_to_top_left = [x_loc, y_loc]
    vector_to_top_right = [x_loc - 1, y_loc]
    vector_to_bottom_left = [x_loc, y_loc - 1]
    vector_to_bottom_right = [x_loc - 1, y_loc - 1]
    #print('найдени вектора до точки - ' + str(vector_to_top_left) + ' ' + str(vector_to_top_right) + ' ' + str(vector_to_bottom_left) + ' ' + str(vector_to_bottom_right))

    sc_tl = scalar_product(vector_to_top_left, top_left_gradient)
    sc_tr = scalar_product(vector_to_top_right, top_right_gradient)
    sc_bl = scalar_product(vector_to_bottom_left, bottom_left_gradient)
    sc_br = scalar_product(vector_to_bottom_right, bottom_right_gradient)
    #print('найдени скалярние произвединия векторов - ' + str(sc_tl) + ' ' + str(sc_tr) + ' ' + str(sc_bl) + ' ' + str(sc_br))

    sm_x = smootherstep(x_loc)
    sm_y = smootherstep(y_loc)
    #print('откоректированое значение - ' + str(sm_x) + ' ' + str(sm_y))

    tx = linear_interpolation(sc_tl, sc_tr, sm_x)
    bx = linear_interpolation(sc_bl, sc_br, sm_x)
    tb = linear_interpolation(tx, bx, sm_y)
    #print('результати интерполяции - ' + str(tx) + ' ' + str(bx) + ' ' + str(tb))

    return tb


def linear_interpolation(a, b, t):
    return a + (b - a) * t


def smootherstep(x):
    return (6 * x ** 5) - (15 * x ** 4) + (10 * x ** 3)


def scalar_product(vect_a, vect_b):
    return (vect_a[0] * vect_b[0]) + (vect_a[1] * vect_b[1])


def create_random_grid():
    grid = []
    for x in range(11):
        grid.append([])
        for y in range(11):
            degree = random.randint(0, 360)
            grid[x].append(convert_degree_in_vector(degree))
    return grid


def convert_degree_in_vector(degree):
    x = math.cos((degree * math.pi) / 180)
    y = math.sin((degree * math.pi) / 180)
    return [x, y]
