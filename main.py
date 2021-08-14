import pygame
import threading
from class_block import CBlock
import perlin_noise
import functions_of_interaction_between_blocks as fibb


def blocks_visualization(block_thread_list, window_thread, window_x_thread, window_y_thread, x_cam_thread,
                         y_cam_thread, length_cam_thread, height_cam_thread, highest_point_thread, filter):
    for block in block_thread_list:
        if block.x + block.size > x_cam_thread and block.x < x_cam_thread + length_cam_thread \
                and block.y + block.size > y_cam_thread and block.y < y_cam_thread + height_cam_thread:
            x_loc = block.x - x_cam_thread
            y_loc = block.y - y_cam_thread

            x = (x_loc / length_cam_thread) * window_x_thread
            y = (y_loc / height_cam_thread) * window_y_thread

            size = (block.size / length_cam_thread) * window_x_thread
            block.draw(window_thread, x, y, size + 1, highest_point_thread, filter)


window_x = 500
window_y = 500
window = pygame.display.set_mode((window_x, window_y))

x_cam = 0
y_cam = 0
length_cam = 1000
height_cam = 1000
zoom = 1

num_horizontal = 100
num_vertical = 100
block_size = 10
block_list = []
new_x = 0
new_y = 0
octave_number = 5
grid_list = []
threads_number = 10

highest_point = 0
extra = 0

filter_list = ["elevation map", "waves map color", "waves map wb", "perlin noise"]
# , "perlin noise"
filter = 0

# for x in range(num_vertical):
#     for y in range(num_horizontal):
#         block_list.append(CBlock(y * block_size, x * block_size, 10, 100, 0, 10, 10, 10))


grid1 = perlin_noise.create_random_grid(5)
grid2 = perlin_noise.create_random_grid(10)
grid3 = perlin_noise.create_random_grid(20)

for column in range(num_vertical):
    for new_block in range(num_horizontal):
        octave1 = perlin_noise.perlin_noise(new_x + 5, new_y + 5, grid1, num_horizontal * block_size) * 20 ** 2 + 100
        octave2 = perlin_noise.perlin_noise(new_x + 5, new_y + 5, grid2, num_horizontal * block_size) * 10 ** 2 + 100
        octave3 = perlin_noise.perlin_noise(new_x + 5, new_y + 5, grid3, num_horizontal * block_size) * 13 ** 2 + 100

        height_block = (octave1 / 2) + (octave2 / 2) + (octave3 / 2)

        block_list.append(CBlock(new_x, new_y, 10, height_block, 0, 10, 10, 10))
        if height_block > highest_point:
            highest_point = height_block

        new_x += block_size
    new_y += block_size
    new_x = 0

block_list[5550].height_water = 10000
# block_list[4550].height_water = 100000
# block_list[3550].height_water = 100000
# block_list[2550].height_water = 100000
# block_list[1550].height_water = 100000
# block_list[5000].height_water = 100000
# block_list[4000].height_water = 100000
# block_list[3000].height_water = 100000
# block_list[2000].height_water = 100000
# block_list[1000].height_water = 100000

# for x in range(len(block_list)):
#     block_list[x].height_water = 1

clock = pygame.time.Clock()
run = True
pygame.init()
while run:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_g:
                filter += 1
                if filter == len(filter_list):
                    filter = 0
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 4:
                if length_cam > 1 and height_cam > 1:
                    new_length_cam = length_cam / 1.2
                    new_height_cam = height_cam / 1.2
                    x_cam += (length_cam - new_length_cam) / 2
                    y_cam += (height_cam - new_height_cam) / 2
                    length_cam = new_length_cam
                    height_cam = new_height_cam
            if e.button == 5:
                new_length_cam = length_cam * 1.2
                new_height_cam = height_cam * 1.2
                x_cam -= (new_length_cam - length_cam) / 2
                y_cam -= (new_height_cam - height_cam) / 2
                length_cam = new_length_cam
                height_cam = new_height_cam
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x_cam += 10
    if keys[pygame.K_a]:
        x_cam -= 10
    if keys[pygame.K_w]:
        y_cam -= 10
    if keys[pygame.K_s]:
        y_cam += 10
    if keys[pygame.K_r]:
        new_length_cam = length_cam * 1.2
        new_height_cam = height_cam * 1.2
        x_cam -= (new_length_cam - length_cam) / 2
        y_cam -= (new_height_cam - height_cam) / 2
        length_cam = new_length_cam
        height_cam = new_height_cam
    if keys[pygame.K_f]:
        if length_cam > 1 and height_cam > 1:
            new_length_cam = length_cam / 1.2
            new_height_cam = height_cam / 1.2
            x_cam += (length_cam - new_length_cam) / 2
            y_cam += (height_cam - new_height_cam) / 2
            length_cam = new_length_cam
            height_cam = new_height_cam

    window.fill((47, 79, 79))

    fibb.water_flow_4(block_list, num_horizontal)

    blocks_for_thread = len(block_list) / threads_number
    block_waiting_list = block_list.copy()
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
    extra += 1

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
    # for block in block_list:
    #     if block.x + block.size > x_cam and block.x < x_cam + length_cam \
    #             and block.y + block.size > y_cam and block.y < y_cam + height_cam:
    #         # x = (block.x - x_cam) * (window_x / length_cam)
    #         # y = (block.y - y_cam) * (window_y / height_cam)
    #         # size = window_x / (length_cam / block.size)
    #         # print("Блок находтса на кординате - {}, {}".format(block.x, block.y))
    #         x_loc = block.x - x_cam
    #         y_loc = block.y - y_cam
    #         # print("кординати камери - {}, {}".format(x_cam, y_cam))
    #         # print("локальные кординати - {}, {}".format(x_loc, y_loc))
    #         x = (x_loc / length_cam) * window_x
    #         y = (y_loc / height_cam) * window_y
    #         # print("размери камери - {}, {}".format(length_cam, height_cam))
    #         # print("x, y - {}, {}".format(x, y))
    #         size = (block.size / length_cam) * window_x
    #         # print("size - {}".format(size))
    #         block.draw(window, x, y, size + 1, highest_point)
    pygame.display.update()
pygame.quit()
