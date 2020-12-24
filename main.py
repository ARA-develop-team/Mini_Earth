import pygame
import random
from class_block import CBlock

window_x = 500
window_y = 500
window = pygame.display.set_mode((window_x, window_y))

x_cam = 0
y_cam = 0
length_cam = window_x
height_cam = window_y
zoom = 1

pygame.init()
num_horizontal = 100
num_vertical = 100
block_size = 10
block_list = []
new_x = 0
new_y = 0
for column in range(num_vertical):
    for new_block in range(num_horizontal):
        block_list.append(CBlock(new_x, new_y, 10, 101, random.randint(99, 101), 10, 10, 10))
        new_x += block_size
    new_y += block_size
    new_x = 0
# block_list.append(CBlock(100, 100, 10, 101, 101, 10, 10, 10))
# block_list.append(CBlock(100, 110, 10, 101, 10, 10, 10, 10))
# block_list.append(CBlock(100, 120, 10, 101, 101, 10, 10, 10))

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x_cam += 1
    if keys[pygame.K_a]:
        x_cam -= 1
    if keys[pygame.K_w]:
        y_cam -= 1
    if keys[pygame.K_s]:
        y_cam += 1
    if keys[pygame.K_r]:
        length_cam += 20
        height_cam += 20
        x_cam -= 10
        y_cam -= 10
    if keys[pygame.K_f]:
        if length_cam > 1 and height_cam > 1:
            length_cam -= 20
            height_cam -= 20
            x_cam += 10
            y_cam += 10

    window.fill((47, 79, 79))
    for block in block_list:
        if block.x + block.size > x_cam and block.x < x_cam + length_cam and block.y + block.size > y_cam and block.y < y_cam + height_cam:
            x = (block.x - x_cam) * (window_x / length_cam)
            y = (block.y - y_cam) * (window_y / height_cam)
            size = window_x / (length_cam / block.size)
            block.draw(window, x, y, size)
    pygame.display.update()
pygame.quit()
