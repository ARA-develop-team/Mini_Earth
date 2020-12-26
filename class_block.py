import pygame


class CBlock(object):
    colorbox = {"Traffic blue": (6, 57, 113),
                "Cobalt blue": (0, 71, 171),
                "Green-blue Crayola": (17, 100, 180),
                "Blue Klein": (58, 117, 196),
                "Blue-gray Crayola": (102, 153, 204)}

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
        self.filter = "elevation map"

    def draw(self, screen, x, y, size, highest_point):
        color = (0, 0, 0)

        if self.filter == "perlin noise":
            rgb = int(self.draw_perlin_noise(highest_point))
            color = (rgb, rgb, rgb)

        if self.filter == "elevation map":
            color = self.draw_elevation_map()

        pygame.draw.rect(screen, color, (x, y, size, size))

    def draw_perlin_noise(self, highest_point):
        if self.height_ground < 1:
            self.height_ground = 1

        percent = (self.height_ground * 100) / highest_point
        return (255 * percent) / 100

    def draw_elevation_map(self):
        water_level = 150
        if self.height_ground < water_level:   # temporarily
            self.height_water = water_level - self.height_ground

        color = (139, 69, 19)

        variation = 20    # height difference of water
        if self.height_water >= 1:
            if self.height_water < variation:
                color = self.colorbox["Blue-gray Crayola"]
            elif self.height_water < variation * 2:
                color = self.colorbox["Blue Klein"]
            elif self.height_water < variation * 3:
                color = self.colorbox["Green-blue Crayola"]
            elif self.height_water < variation * 4:
                color = self.colorbox["Cobalt blue"]
            else:
                color = self.colorbox["Traffic blue"]

        return color
