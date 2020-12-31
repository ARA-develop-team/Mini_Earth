import pygame


class CBlock(object):
    run = True
    screen = None
    filter = None
    highest_point = None
    colorbox = {"Traffic blue": (6, 57, 113),
                "Cobalt blue": (0, 71, 171),
                "Green-blue Crayola": (17, 100, 180),
                "Blue Klein": (58, 117, 196),
                "Blue-gray Crayola": (102, 153, 204),

                "Pearl green": (0, 70, 0),
                "Dark spring green": (0, 100, 0),
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
                "Byzantium": (112, 41, 99)}

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
        self.wave_counter = 0
        self.variation = 18     # height difference of place
        self.color = (0, 0, 0)

    def draw(self, x, y, size):
        if self.color == (0, 0, 0):
            self.color = (0, 200, 0)
        pygame.draw.rect(self.screen, self.color, (x, y, size, size))

    def color_selection(self):
        if self.filter == "perlin noise":
            self.draw_perlin_noise()

        elif self.filter == "elevation map":
            self.draw_elevation_map(True)

        elif self.filter == "waves map color":
            self.draw_waves_map_color()

        elif self.filter == "waves map wb":
            self.draw_waves_map_wb()

        else:
            print("smth wrong")

    def draw_perlin_noise(self):
        if self.height_ground < 1:
            self.height_ground = 1

        percent = (self.height_ground * 100) / self.highest_point
        rgb = (255 * percent) / 100
        self.color = (rgb, rgb, rgb)

    def draw_elevation_map(self, status):

        if self.height_water > 0 and status:
            if self.height_water < self.variation:
                self.color = self.colorbox["Blue-gray Crayola"]
            elif self.height_water < self.variation * 2:
                self.color = self.colorbox["Blue Klein"]
            elif self.height_water < self.variation * 3:
                self.color = self.colorbox["Green-blue Crayola"]
            elif self.height_water < self.variation * 4:
                self.color = self.colorbox["Cobalt blue"]
            else:
                self.color = self.colorbox["Traffic blue"]
        else:
            if self.height_ground < self.variation * 2:
                self.color = self.colorbox["Pearl green"]
            elif self.height_ground < self.variation * 4:
                self.color = self.colorbox["Dark spring green"]
            elif self.height_ground < self.variation * 6:
                self.color = self.colorbox["Green"]
            elif self.height_ground < self.variation * 8:
                self.color = self.colorbox["Muslim green"]
            elif self.height_ground < self.variation * 10:
                self.color = self.colorbox["Verdejo green"]
            elif self.height_ground < self.variation * 12:
                self.color = self.colorbox["Pear green"]
            elif self.height_ground < self.variation * 14:
                self.color = self.colorbox["Golden birch"]
            else:
                self.color = self.colorbox["Redhead"]

    def draw_waves_map_color(self):
        if self.height_water > 0:
            if self.wave_counter > 30:
                self.color = self.colorbox["Scarlet"]
            elif self.wave_counter > 25:
                self.color = self.colorbox["Red-orange Crayola"]
            elif self.wave_counter > 20:
                self.color = self.colorbox["Bittersweet"]
            elif self.wave_counter > 15:
                self.color = self.colorbox["Neon carrot"]
            elif self.wave_counter > 10:
                self.color = self.colorbox["Lemon-yellow Crayola"]
            elif self.wave_counter > 5:
                self.color = self.colorbox["Moderate aquamarine"]
            elif self.wave_counter > 0:
                self.color = self.colorbox["Blue screen of death"]
            # elif self.wave_counter > -5:
            #     color = self.colorbox["Byzantine"]
            # elif self.wave_counter > -15:
            #     color = self.colorbox["Dark magenta"]
            # elif self.wave_counter < -15:
            #     color = self.colorbox["Byzantium"]
            else:
                self.color = (0, 0, 0)
        else:
            self.draw_elevation_map(False)

    def draw_waves_map_wb(self):
        if self.height_water > 0:
            rgb = (255 / 50) * self.wave_counter
            if rgb > 255:
                rgb = 255
            self.color = (rgb, rgb, rgb)
        else:
            self.draw_elevation_map(False)
