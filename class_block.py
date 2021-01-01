import pygame


class CBlock(object):
    colorbox = {"Traffic blue": (6, 57, 113),
                "Cobalt blue": (0, 71, 171),
                "Green-blue Crayola": (17, 100, 180),
                "Blue Klein": (58, 117, 196),
                "Blue-gray Crayola": (102, 153, 204),

                "Dark spring green": (0, 100, 0),
                "Pearl green": (0, 70, 0),
                "Green": (0, 128, 0),
                "Muslim green": (0, 153, 0),
                "Verdejo green": (52, 201, 36),
                "Pear green": (209, 226, 49),
                "Golden birch": (218, 165, 32),
                "Redhead": (215, 125, 49),

                "Bittersweet": (255, 131, 115),
                "Red-orange Crayola": (255, 83, 73),
                "Scarlet": (255, 36, 0),
                "Neon carrot": (255, 163, 67),
                "Lemon-yellow Crayola": (255, 244, 79),
                "Moderate aquamarine": (102, 205, 170),
                "Blue screen of death": (18, 47, 170),
                "Gray squirrel": (120, 133, 139),
                "Yellow ocher": (174, 160, 75),
                "Byzantine": (210, 53, 210),
                "Dark magenta": (139, 0, 139),
                "Byzantium":(112, 41, 99)}

    def __init__(self, x, y, size, height_ground, height_water, temp_surface, temp_air, clouds):
        self.x = x
        self.y = y
        self.size = size
        self.height_ground = height_ground
        self.height_water = height_water
        self.temp_surface = temp_surface
        self.temp_air = temp_air
        self.future_temp_air = 0
        self.cloud_concentration = clouds
        self.vegetation = []
        self.isDay = True
        self.filter = "waves map"
        self.wave_counter = 0
        self.future_hw = 0

    def draw(self, screen, x, y, size, highest_point, filter):
        color = (0, 0, 0)
        self.filter = filter

        if self.filter == "perlin noise":
            rgb = int(self.draw_perlin_noise(highest_point))
            color = (rgb, rgb, rgb)

        if self.filter == "elevation map":
            color = self.draw_elevation_map()

        if self.filter == "waves map color":
            color = self.draw_waves_map_color()

        if self.filter == "waves map wb":
            color = self.draw_waves_map_wb()

        if self.filter == "temperature air":
            color = self.draw_temperature_air()
        pygame.draw.rect(screen, color, (x, y, size, size))

    def draw_perlin_noise(self, highest_point):
        if self.height_ground < 1:
            self.height_ground = 1

        percent = (self.height_ground * 100) / highest_point
        return (255 * percent) / 100

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
        rgb = self.temp_air
        if rgb > 255:
            rgb = 255
        if rgb < 0:
            rgb = 0
        color = (int(rgb), 0, 0)
        return color

    def assignment_of_values(self):
        self.height_water += self.future_hw
        self.future_hw = 0

        self.temp_air += self.future_temp_air
        self.future_temp_air = 0
