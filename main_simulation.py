"""Main World file"""

from parser import parse_data
from class_block import CBlock
import perlin_noise


class Simulation(object):

    def __init__(self):
        self.run = True
        self.active_filter = 0

        data = parse_data('data.yml')
        self.filters = data['filters']

        self.window_size = (data['window_x'], data['window_y'])
        self.camera_position = (data['camera_x'], data['camera_y'])

        self.block_num_horizontal = data['block_num_columns']
        self.block_num_vertical = data['block_num_raws']
        self.block_size = data['block_size']

        self.camera = None
        self.world = None
        self.create_blocks

        del data

    def create_blocks(self):
        """create all blocks using perlin noise"""

        blocks = []
        
        grid_list = []
        grid_number = 5 

        for _ in range(3):
            grid_list.append(perlin_noise.create_random_grid(grid_number))
            grid_number *= 2

        octave_list = []

        for y in range(self.block_num_vertical):
            y = y * self.block_size

            for x in range(self.block_num_horizontal):
                x = x * self.block_size
                
                for i in range(len(grid_list)):
                    octave_list.append(perlin_noise.perlin_noise(x + 5, y + 5, grid_list[i], 
                        self.block_grid_size[0] * self.block_size)) * (20 - 5*i) ** 2 + 100

                height_block = 0
                for octave in octave_list:
                     height_block += octave / 2

                blocks.append(CBlock(x, y, self.block_size, height_block, 0, 10, -50, 10))

        return blocks


if __name__ == '__main__':
    simulation = Simulation()
    
                    

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
    #     # if keys[pygame.K_g]:


