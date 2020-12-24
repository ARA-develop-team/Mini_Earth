import pygame


class CBlock(object):
    def __init__(self, x, y, size, height_ground, height_water, temp_surface, temp_air, clouds):
        self.x = x
        self.y = y
        self.size = size
        self.height_ground = height_ground
        self.height_water = height_water
        self.temp_surface = temp_surface
        self.temp_air = temp_air
        self.cloud_concentration = clouds
        self.vegetation = []
        self.isDay = True

    def draw(self, screen, x, y, size):
        color = (139, 69, 19)
        if self.height_water > 100:
            color = (30, 144, 255)
        pygame.draw.rect(screen, color, (x, y, size, size))

