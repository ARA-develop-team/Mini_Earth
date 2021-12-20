
class Planet(object):

    def __init__(self, block_list, num_horizontal, num_vertical, block_size, highest):
        self.block_list = block_list
        self.block_size = block_size
        self.num_horizontal = num_horizontal
        self.num_vertical = num_vertical
        self.highest_point = highest

    def fibb_main(self):
        for number in range(len(self.block_list)):
            if number % self.num_horizontal == self.num_horizontal - 1:
                dif1 = water_flow_between_block(self.block_list[number], self.block_list[number - self.num_horizontal + 1])
                dif2 = water_flow_between_block(self.block_list[number], self.block_list[number - 1])

            elif number % self.num_horizontal == 0:
                dif1 = water_flow_between_block(self.block_list[number], self.block_list[number + self.num_horizontal - 1])
                dif2 = water_flow_between_block(self.block_list[number], self.block_list[number + 1])

            else:
                dif1 = water_flow_between_block(self.block_list[number], self.block_list[number + 1])
                dif2 = water_flow_between_block(self.block_list[number], self.block_list[number - 1])

            if 0 <= number <= self.num_horizontal - 1:
                dif3 = water_flow_between_block(self.block_list[number], self.block_list[number + self.num_horizontal])
                dif4 = dif3

            elif len(self.block_list) - self.num_horizontal <= number < len(self.block_list):
                dif3 = water_flow_between_block(self.block_list[number], self.block_list[number - self.num_horizontal])
                dif4 = dif3

            else:
                dif3 = water_flow_between_block(self.block_list[number], self.block_list[number + self.num_horizontal])
                dif4 = water_flow_between_block(self.block_list[number], self.block_list[number - self.num_horizontal])

            self.block_list[number].wave_counter = dif1 + dif2 + dif3 + dif4


def water_flow_between_block(block1, block2):
    difference = (block1.height_ground + block1.height_water) \
                 - (block2.height_ground + block2.height_water)
    if difference > 0:
        flow = difference * 0.2
        if block1.height_water < flow:
            flow = block1.height_water * 0.2
            block1.future_hw -= flow
            block2.future_hw += flow

        else:
            block1.future_hw -= flow
            block2.future_hw += flow

    if block2.height_water == 0:
        return 0
    else:
        return abs(difference)
