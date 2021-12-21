import pygame
from colors import colors


class Block(object):
    colorbox = colors
    highest_point = None

    def __init__(self, x, y, size, height_ground, height_water, temp_surface, temp_air, clouds):
        # self.x = x
        # self.y = y
        # self.size = size
        self.height_ground = height_ground
        self.height_water = height_water
        # self.temp_surface = temp_surface
        self.temp_air = temp_air
        # self.future_temp_air = 0
        # self.cloud_concentration = clouds
        # self.vegetation = []
        # self.isDay = True
        # self.filter = "waves map"
        # self.wave_counter = 0
        # self.future_hw = 0

    # def assignment_of_values(self):
    #     self.height_water += self.future_hw
    #     self.future_hw = 0
    #
    #     self.temp_air += self.future_temp_air
    #     self.future_temp_air = 0
    #
    # def pib(self):
    #     temp_difference = self.temp_surface - self.temp_air
    #     self.temp_air += (temp_difference * 20) / 100
    #     self.temp_surface -= (temp_difference * 5) / 100

    # def draw(self, screen, x, y, size, highest_point, filter):
    #     color = (0, 0, 0)
    #     self.filter = filter
    #
    #     if self.filter == "perlin noise":
    #         color = self.draw_perlin_noise()
    #
    #     if self.filter == "elevation map":
    #         color = self.draw_elevation_map()
    #
    #     if self.filter == "waves map color":
    #         color = self.draw_waves_map_color()
    #
    #     if self.filter == "waves map wb":
    #         color = self.draw_waves_map_wb()
    #
    #     if self.filter == "temperature air":
    #         color = self.draw_temperature_air()
    #
    #     pygame.draw.rect(screen, color, (x, y, size, size))

    def draw_perlin_noise(self):
        if self.height_ground < 1:
            self.height_ground = 1

        percent = (self.height_ground * 100) / self.highest_point

        rgb = int((255 * percent) / 100)
        color = (rgb, rgb, rgb)
        return color

    def draw_elevation_map(self):
        variation = 18    # height difference of place

        if self.height_water > 0:
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
        else:
            if self.height_ground < variation * 2:
                color = self.colorbox["Pearl green"]
            elif self.height_ground < variation * 4:
                color = self.colorbox["Dark spring green"]
            elif self.height_ground < variation * 6:
                color = self.colorbox["Green"]
            elif self.height_ground < variation * 8:
                color = self.colorbox["Muslim green"]
            elif self.height_ground < variation * 10:
                color = self.colorbox["Verdejo green"]
            elif self.height_ground < variation * 12:
                color = self.colorbox["Pear green"]
            elif self.height_ground < variation * 14:
                color = self.colorbox["Golden birch"]
            else:
                color = self.colorbox["Redhead"]
        return color

    def draw_waves_map_color(self):
        water_level = 150
        variation = 20

        if self.height_water > 0:
            if self.wave_counter > 30:
                color = self.colorbox["Scarlet"]
            elif self.wave_counter > 25:
                color = self.colorbox["Red-orange Crayola"]
            elif self.wave_counter > 20:
                color = self.colorbox["Bittersweet"]
            elif self.wave_counter > 15:
                color = self.colorbox["Neon carrot"]
            elif self.wave_counter > 10:
                color = self.colorbox["Lemon-yellow Crayola"]
            elif self.wave_counter > 5:
                color = self.colorbox["Moderate aquamarine"]
            elif self.wave_counter > 0:
                color = self.colorbox["Blue screen of death"]
            # elif self.wave_counter > -5:
            #     color = self.colorbox["Byzantine"]
            # elif self.wave_counter > -15:
            #     color = self.colorbox["Dark magenta"]
            # elif self.wave_counter < -15:
            #     color = self.colorbox["Byzantium"]
            else:
                color = (0, 0, 0)
        else:
            elevation = self.height_ground - water_level
            if elevation < variation:
                color = self.colorbox["Green"]
            elif elevation < variation * 2:
                color = self.colorbox["Muslim green"]
            elif elevation < variation * 3:
                color = self.colorbox["Verdejo green"]
            elif elevation < variation * 4:
                color = self.colorbox["Pear green"]
            elif elevation < variation * 5:
                color = self.colorbox["Golden birch"]
            else:
                color = self.colorbox["Redhead"]
        return color

    def draw_waves_map_wb(self):
        water_level = 150
        variation = 20

        if self.height_water > 0:
            rgb = (255 / 50) * self.wave_counter
            if rgb > 255:
                rgb = 255
            if rgb < 0:
                rgb = 0
            color = (rgb, rgb, rgb)

        else:
            elevation = self.height_ground - water_level
            if elevation < variation:
                color = self.colorbox["Green"]
            elif elevation < variation * 2:
                color = self.colorbox["Muslim green"]
            elif elevation < variation * 3:
                color = self.colorbox["Verdejo green"]
            elif elevation < variation * 4:
                color = self.colorbox["Pear green"]
            elif elevation < variation * 5:
                color = self.colorbox["Golden birch"]
            else:
                color = self.colorbox["Redhead"]
        return color

    def draw_temperature_air(self):
        if self.temp_air > 0:
            rgb = (255 / 30) * self.temp_air
            if rgb > 255:
                rgb = 255
            if rgb < 0:
                rgb = 0
            color = (rgb, 0, 0)

        else:
            rgb = (255 / 30) * abs(self.temp_air)
            if rgb > 255:
                rgb = 255
                if rgb < 0:
                    rgb = 0
            color = (0, 0, rgb)
        return color


