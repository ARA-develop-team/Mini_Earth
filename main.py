import pygame

window_x = 500
window_y = 500
window = pygame.display.set_mode((window_x, window_y))

x_cam = 0
y_cam = 0
length_cam = window_x
height_cam = window_y

pygame.init()
block_list = []
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

    window.fill((47, 79, 79))
    for block in block_list:
        if block.x + block.height > x_cam and x_b < x_cam + length_cam and block.y + block.height > y_cam and block.y < y_cam + heigth_cam:
            block.draw(block.x - x_cam, block.y - y_cam)
    pygame.display.update()
pygame.quit()
