"""Main World file.


* Comment for developers!

For a better understanding of each other, I propose you such an agreement:
    - Let’s mark all time comments with the star symbol (*). Example:

      # * Delete in the future.

      I mean the commentaries you’ve created for yourself and which are you going to
      delete in the future. Normal comments leave with no changes :)
"""

import pygame
import pickle
import perlin_noise
# import analysis

from decorators import ProgressBar
from parser import parse_data
from class_block import Block
from planet import Planet


print("Hello from the ARA development. https://github.com/ARA-develop-team")
pygame.init()


class Simulation(object):

    def __init__(self):
        self.run = True

        data = parse_data('data.yml')

        self.active_filter = 0
        self.filters = data['filters']

        self.window_size = (data['window_x'], data['window_y'])
        self.camera_position = (data['camera_x'], data['camera_y'])

        self.block_num_horizontal = data['block_num_columns']
        self.block_num_vertical = data['block_num_rows']
        self.block_size = data['block_size']

        self.camera = None

        self.map = []  # list with colors
        self.world = self.create_world(data['grid_value'], data['octave_value'])

        self.window = pygame.display.set_mode(self.window_size)
        # pygame.display.set_caption('Mini Earth')

        self.clock = pygame.time.Clock()

        del data

    def main(self):
        """Main function."""
        # self.world.block_list[50][80].height_water = 100000
        while self.run:
            self.input_process()
            # self.world.block_list[30][50].height_water += 2

            filter_function = select_filter_function(self.filters[self.active_filter])
            self.world.iteration(filter_function)

            self.draw_world()

    def draw_map(self):
        """Draw list of colors."""

        color_counter = 0
        for y in range(self.block_num_vertical):
            y = y * self.block_size

            for x in range(self.block_num_horizontal):
                x = x * self.block_size

                pygame.draw.rect(self.window, self.map[color_counter][0], (x, y, self.block_size, self.block_size))
                color_counter += 1

    def draw_world(self):
        """Draw the World using pygame."""
        self.clock.tick(30)
        pygame.display.set_caption(f"FPS: {self.clock.get_fps()}")

        self.window.fill((47, 79, 79))
        self.draw_map()
        pygame.display.flip()

    def input_process(self):
        """Process all pygame inputs from user."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def create_world(self, *args):
        """Create the World."""

        blocks = self.create_blocks(*args)
        highest_point = find_highest_block(blocks)
        Block.highest_point = highest_point

        world = Planet(blocks, self.block_num_horizontal, self.block_num_vertical, self.block_size, highest_point)

        return world

    def create_blocks(self, grid_value, octave_extra_value):
        """Create all blocks using perlin noise."""

        blocks = []
        grid_list = []

        @ProgressBar(text="Creating Perlin Grids", aim=len(grid_value))
        def create_perlin_grid(grid_size):
            grid = perlin_noise.create_random_grid(grid_size)
            return grid

        def deploy_to_map():
            default_color = (0, 0, 0)
            self.map.append([default_color])

        @ProgressBar(text='Creating Blocks', aim=(self.block_num_horizontal * self.block_num_vertical))
        def create_block():
            octave_list = []

            for i in range(len(grid_list)):
                new_octave = perlin_noise.perlin_noise(x + 5, y + 5, grid_list[i],
                                                       self.block_num_horizontal * self.block_size)

                octave_list.append(new_octave * octave_extra_value[i] ** 2 + 100)

            # Find height of ground in the block.
            height_block = 0
            for octave in octave_list:
                height_block += octave / 2

            block = Block(x, y, self.block_size, height_block, 0, 10, -50, 10, self.map[-1])

            # # ---
            # if len(blocks[-1]) == self.block_num_horizontal - 30:
            #     block = Block(x, y, self.block_size, 100, 0, 10, -50, 10, self.map[-1])
            # else:
            #     block = Block(x, y, self.block_size, 10, 0, 10, -50, 10, self.map[-1])
            # # ---

            return block

        # Code of creation.
        for value in grid_value:
            new_grid = create_perlin_grid(value)
            grid_list.append(new_grid)

        for y in range(self.block_num_vertical):
            y = y * self.block_size
            blocks.append([])

            for x in range(self.block_num_horizontal):
                x = x * self.block_size

                deploy_to_map()
                new_block = create_block()
                blocks[-1].append(new_block)

        return blocks

    def closing(self):
        water = 0
        height_list = []
        for line in self.world.block_list:
            for block in line:
                water += block.height_water
                height_list.append(block.height_water)
        print(water)
        pygame.quit()


def select_filter_function(current_filter):
    """Choose function, which is responsible for current filter."""

    if current_filter == "perlin noise":
        return Block.draw_perlin_noise

    elif current_filter == "elevation map":
        return Block.draw_elevation_map

    elif current_filter == "waves map color":
        return Block.draw_waves_map_color

    elif current_filter == "waves map wb":
        return Block.draw_waves_map_wb

    elif current_filter == "temperature air":
        return Block.draw_temperature_air

    else:
        raise NameError


def find_highest_block(blocks):
    """Find the highest block in the world."""

    highest = 0

    for line in blocks:
        for block in line:
            if block.height_ground > highest:
                highest = block.height_ground

    return highest


def save(data):
    """Save simulation for reopening."""

    with open('world.pkl', 'wb') as file:
        pickle.dump(data, file, pickle.HIGHEST_PROTOCOL)


def load():
    """Load last closed simulation."""

    with open('world.pkl', 'rb') as file:
        return pickle.load(file)


if __name__ == '__main__':
    print("\nWelcome to the World!")

    simulation = Simulation()
    simulation.main()

    simulation.closing()
    # analysis.show_graph([3, 3, 3, 5])

    # def preparing_blocks(blocks):
    #     """Find the highest block in the world and find block's neighbors."""
    #     highest = 0
    #
    #     for y in range(len(blocks)):
    #         for x in range(len(blocks[y])):
    #             block = blocks[y][x]
    #
    #             # top and bottom neighbors
    #             if y == 0:
    #                 block.neighbors.append(blocks[y + 1][x])
    #
    #             elif y == len(blocks) - 1:
    #                 block.neighbors.append(blocks[y - 1][x])
    #
    #             else:
    #                 block.neighbors.append(blocks[y - 1][x])
    #                 block.neighbors.append(blocks[y + 1][x])
    #
    #             # left and right neighbors
    #             if x == 0:
    #                 block.neighbors.append(blocks[y][x + 1])
    #                 block.neighbors.append(blocks[y][len(blocks[y]) - 1])
    #
    #             elif x == len(blocks[y]) - 1:
    #                 block.neighbors.append(blocks[y][x - 1])
    #                 block.neighbors.append(blocks[y][0])
    #
    #             else:
    #                 block.neighbors.append(blocks[y][x + 1])
    #                 block.neighbors.append(blocks[y][x - 1])
    #
    #             # check if highest block
    #             if block.height_ground > highest:
    #                 highest = block.height_ground

    # return highest

    # def input_mouse(self):
    #
    #     for e in pygame.event.get():  # проверка нажатий
    #         if e.type == pygame.QUIT:
    #             self.run = False
    #
    #         if e.type == pygame.MOUSEBUTTONUP:
    #             if e.button == 1:
    #                 panel.press_buttons(e.pos)
    #                 self.filter = panel.press_filter_buttons(e.pos, filter)
    #
    #         # if e.type == pygame.MOUSEBUTTONDOWN:
    #         #     if e.button == 4:
    #         #         if length_cam > 1 and height_cam > 1:
    #         #
    #         #     if e.button == 5:
    #
