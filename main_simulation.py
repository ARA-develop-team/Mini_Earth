"""Main World file.


* Comment for developers!

For a better understanding of each other, I propose you such an agreement:
    - Let’s mark all time comments with the star symbol (*). Example:

      # * Delete in the future.

      I mean the commentaries you’ve created for yourself and which are you going to
      delete in the future. Normal comments leave with no changes :)
"""

import time
import pygame
import pickle
import perlin_noise

from decorators import ProgressBar
from parser import parse_data
from class_block import CBlock
from planet import Planet

print("Hello from the ARA development. https://github.com/ARA-develop-team")


class Simulation(object):

    def __init__(self):
        self.run = True

        data = parse_data('data.yml')
        if not data:
            quit()

        self.active_filter = 0
        self.filters = data['filters']

        self.window_size = (data['window_x'], data['window_y'])
        self.camera_position = (data['camera_x'], data['camera_y'])

        self.block_num_horizontal = data['block_num_columns']
        self.block_num_vertical = data['block_num_rows']
        self.block_size = data['block_size']

        self.camera = None

        self.world = self.create_world(data['grid_value'], data['octave_value'])

        pygame.init()
        self.window = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption('Mini Earth')

        del data

    def main(self):
        """Main function."""

        while self.run:
            self.input_process()
            self.draw_world()

    def temp(self):
        for line in self.world.block_list:
            for block in line:
                block.draw(self.window, block.x, block.y, block.size, self.world.highest_point,
                           self.filters[self.active_filter])

    def draw_world(self):
        """Draw the World using pygame."""

        self.window.fill((47, 79, 79))
        self.temp()
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

            block = CBlock(x, y, self.block_size, height_block, 0, 10, -50, 10)
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

                new_block = create_block()
                blocks[-1].append(new_block)

        return blocks


def find_highest_block(blocks):
    """Find the highest block in the world."""

    highest = 0

    for line in blocks:
        for block in line:
            if block.height_ground > highest:
                highest = block.height_ground

    return highest


def save(data):
    """Save simulation for reopening"""

    with open('world.pkl', 'wb') as file:
        pickle.dump(data, file, pickle.HIGHEST_PROTOCOL)


def load():
    """Load last closed simulation"""
    with open('world.pkl', 'rb') as file:
        return pickle.load(file)


if __name__ == '__main__':
    print("\nWelcome to the World!")
    simulation = Simulation()
    simulation.main()

    # simulation.main()

    # def create_word_with_perlin_noise(self):
    #     pass
    #
    # def draw_menu(self):
    #     pass
    #
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
    #
    # def input_keyboard(self):
    #     keys = pygame.key.get_pressed()
    #     # if keys[pygame.K_d]:
    #     #
    #     # if keys[pygame.K_a]:
    #     #
    #     # if keys[pygame.K_w]:
    #     #
    #     # if keys[pygame.K_s]:
    #     #
    #     # if keys[pygame.K_r]:
    #     #
    #     # if keys[pygame.K_f]:
    #     #
    #
