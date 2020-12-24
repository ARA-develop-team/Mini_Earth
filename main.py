import pygame
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
block_list = []
block_list.append(CBlock(100, 100, 10, 101, 101, 10, 10, 10))
block_list.append(CBlock(100, 110, 10, 101, 10, 10, 10, 10))
block_list.append(CBlock(100, 120, 10, 101, 101, 10, 10, 10))
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x_cam += 0.5
    if keys[pygame.K_a]:
        x_cam -= 0.5
    if keys[pygame.K_w]:
        y_cam -= 0.5
    if keys[pygame.K_s]:
        y_cam += 0.5

    window.fill((47, 79, 79))
    for block in block_list:
        if block.x + block.size > x_cam and block.x < x_cam + length_cam and block.y + block.size > y_cam and block.y < y_cam + height_cam:
            block.draw(window, block.x - x_cam, block.y - y_cam, block.size)
    pygame.display.update()
pygame.quit()
