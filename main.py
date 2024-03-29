import pygame
import threading
from class_block import Block
import perlin_noise
import functions_of_interaction_between_blocks as fibb
import time
import panel
import camera
import planet

threads_number = 10  # количество потоков

# переменные для window (pygame)
window_x = 1000
window_y = 1000
window_x_map = (window_x * 75) / 100
window_y_map = window_y
window_x_panel = (window_x * 25) / 100
window_y_panel = window_y
x_panel = (window_x * 75) / 100
y_panel = 0
window = pygame.display.set_mode((window_x, window_y))

# # переменнные камеры
main_camera = camera.Camera(0, 0, window_x_map * 0.1, window_y_map * 0.1)

x_cam = 0  # координаты камеры
y_cam = 0
length_cam = window_x_map * 0.1  # длина и высота камеры
height_cam = window_y_map * 0.1
zoom = 1

# переменнные блоков
num_horizontal = 100  # количество блоков по горизонтали
num_vertical = 100  # количество блоков по вертикали
block_size = 10  # размер блока
block_list = []  # лист класов блок


# переменные для работы с шумом
new_x = 0
new_y = 0
grid_list = []

# переменные для фильтров
filter = 0
filter_list = ["elevation map", "waves map color", "waves map wb", "perlin noise", "temperature air"]

sun_pos = 5000
sun_range = 50

highest_point = 0
extra = 0


# прорисовка блоков которые видит камера
def blocks_visualization(block_thread_list, window_thread, window_x_thread, window_y_thread, x_cam_thread,
                         y_cam_thread, length_cam_thread, height_cam_thread, highest_point_thread, filter):
    for block in block_thread_list:  # перебор блоков
        block.assignment_of_values()
        # проверка видит ли камера блок
        if main_camera.in_vision(block.x, block.y, block.size):
            x, y, size = main_camera.get_block_in_window(block.x, block.y, block.size, window_x_thread, window_y_thread)
            block.draw(window_thread, x, y, size + 1, highest_point_thread, filter)



# for column in range(num_vertical):
#
#     for new_block in range(num_horizontal):
#         block_list.append(CBlock(new_x, new_y, 10, 20, 0, 10, -50, 10))
#         new_x += 1
#     new_y += 1
#     new_x = 0
# highest_point = 20
# block_list[55].height_water = 10

# создание блоков с шумом перлина
grid1 = perlin_noise.create_random_grid(5)
grid2 = perlin_noise.create_random_grid(10)
grid3 = perlin_noise.create_random_grid(20)

for column in range(num_vertical):
    for new_block in range(num_horizontal):
        octave1 = perlin_noise.perlin_noise(new_x + 5, new_y + 5, grid1, num_horizontal * block_size) * 20 ** 2 + 100
        octave2 = perlin_noise.perlin_noise(new_x + 5, new_y + 5, grid2, num_horizontal * block_size) * 10 ** 2 + 100
        octave3 = perlin_noise.perlin_noise(new_x + 5, new_y + 5, grid3, num_horizontal * block_size) * 13 ** 2 + 100

        height_block = (octave1 / 2) + (octave2 / 2) + (octave3 / 2)

        block_list.append(Block(new_x, new_y, 10, height_block, 0, 10, -50, 10))
        if height_block > highest_point:
            highest_point = height_block

        new_x += block_size
    new_y += block_size
    new_x = 0

word = planet.Planet(block_list, num_horizontal, num_vertical, block_size)

# заполнение блоков водой
word.block_list[5550].height_water = 10000
word.block_list[4550].height_water = 10000
word.block_list[3550].height_water = 10000
word.block_list[2550].height_water = 10000
word.block_list[1550].height_water = 10000
word.block_list[5000].height_water = 10000
word.block_list[4000].height_water = 10000
word.block_list[3000].height_water = 10000
word.block_list[2000].height_water = 10000
word.block_list[1000].height_water = 10000

# block_list[2050].temp_air = 30

clock = pygame.time.Clock()  # для ограничения скорости цикла

run = True

panel = panel.Panel(x_panel, y_panel, window_x_panel, window_y_panel)  # создание панели

pygame.init()
while run:
    clock.tick(60)
    for e in pygame.event.get():  # проверка нажатий
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_g:
                filter += 1
                if filter == len(filter_list):
                    filter = 0

        if e.type == pygame.MOUSEBUTTONUP:
            if e.button == 1:
                panel.press_buttons(e.pos)
                filter = panel.press_filter_buttons(e.pos, filter)


        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 4:
                main_camera.zoom_in()
            if e.button == 5:
                main_camera.zoom_out()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        main_camera.move_right(10)
    if keys[pygame.K_a]:
        main_camera.move_left(10)
    if keys[pygame.K_w]:
        main_camera.move_up(10)
    if keys[pygame.K_s]:
        main_camera.move_down(10)
    if keys[pygame.K_r]:
        main_camera.zoom_out()
    if keys[pygame.K_f]:
        main_camera.zoom_in()

    window.fill((47, 79, 79))

    blocks_for_thread = len(word.block_list) / threads_number
    block_waiting_list = word.block_list.copy()
    draw_thread_list = []

    for thread in range(threads_number):
        block_list_for_thread = []
        if len(block_waiting_list) != 0:
            for block in range(int(blocks_for_thread)):
                block_list_for_thread.append(block_waiting_list.pop())

            draw_thread = threading.Thread(target=blocks_visualization, args=(block_list_for_thread, window, window_x,
                                                                              window_y, x_cam, y_cam, length_cam,
                                                                              height_cam, highest_point,
                                                                              filter_list[filter]))
            draw_thread_list.append(draw_thread)
            draw_thread.start()

    thread_working = True

    while thread_working:
        if len(draw_thread_list) == 0:
            thread_working = False

        for thread in draw_thread_list:
            if not thread.is_alive():
                thread.join()
                draw_thread_list.remove(thread)
            if len(draw_thread_list) == 0:
                thread_working = False
                break

    if not panel.pause:
        word.fibb_main()
        if sun_pos == 5100:
            sun_pos = 5000
        else:
            sun_pos += 1

    # for line in range(sun_range):
    #     for number in range(sun_range):
    #         block_list[sun_pos + number].temp_surface += 10

    # blocks_for_thread = len(block_list) / threads_number
    # block_waiting_list = block_list.copy()
    # draw_thread_list = []
    #
    # for thread in range(threads_number):
    #     block_list_for_thread = []
    #     if len(block_waiting_list) != 0:
    #         for block in range(int(blocks_for_thread)):
    #             block_list_for_thread.append(block_waiting_list.pop())
    #
    #         draw_thread = threading.Thread(target=blocks_visualization, args=(block_list_for_thread, window, window_x,
    #                                                                           window_y, x_cam, y_cam, length_cam,
    #                                                                           height_cam, highest_point,
    #                                                                           filter_list[filter]))
    #         draw_thread_list.append(draw_thread)
    #         draw_thread.start()
    #
    # thread_working = True
    # extra += 1
    #
    # while thread_working:
    #     if len(draw_thread_list) == 0:
    #         thread_working = False
    #
    #     for thread in draw_thread_list:
    #         if not thread.is_alive():
    #             thread.join()
    #             draw_thread_list.remove(thread)
    #         if len(draw_thread_list) == 0:
    #             thread_working = False
    #             break
    panel.draw_panel(window)

    pygame.display.update()
pygame.quit()
