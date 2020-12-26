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
        self.counter = 100
        self.filter = " "

    def draw(self, screen, x, y, size, highest_point):
        # rgb = int(self.draw_perlin_noise(highest_point))
        # color = (rgb, rgb, rgb)
        # print(rgb)

        color = self.draw_elevation_map()
        pygame.draw.rect(screen, color, (x, y, size, size))

    def draw_perlin_noise(self, highest_point):
        if self.height_ground < 1:
            self.height_ground = 1
        if self.height_ground > 300:
            self.height_ground = 299
        percent = (self.height_ground * 100) / highest_point
        return (255 * percent) / 100

    def draw_elevation_map(self):
        color = (139, 69, 19)
        # if self.height_water > 100:
        #     color = (30, 144, 255)
        # self.counter += 1
        if self.height_ground < self.counter:
            color = (30, 144, 255)

        return color
