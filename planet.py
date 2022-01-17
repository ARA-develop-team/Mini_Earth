class Planet(object):

    def __init__(self, block_list, num_horizontal, num_vertical, block_size, highest):
        self.block_list = block_list
        self.block_size = block_size
        self.num_horizontal = num_horizontal
        self.num_vertical = num_vertical
        self.highest_point = highest

    def iteration(self, current_filter):
        """Causes a block queue to be executed."""

        for j in range(self.num_vertical - 1):
            processing_block(self.block_list[j][0], current_filter,
                             self.block_list[j + 1][0], self.block_list[j][1],
                             self.block_list[j][self.num_vertical - 1])

        for j in range(self.num_vertical - 1):
            for i in range(1, self.num_horizontal - 1):
                processing_block(self.block_list[j][i], current_filter,
                                 self.block_list[j + 1][i], self.block_list[j][i + 1])

        for j in range(self.num_vertical - 1):
            processing_block(self.block_list[j][self.num_horizontal - 1], current_filter,
                             self.block_list[j + 1][self.num_horizontal - 1])

        for i in range(self.num_horizontal - 1):
            processing_block(self.block_list[self.num_vertical - 1][i], current_filter,
                             self.block_list[self.num_vertical - 1][i + 1])

        processing_block_without_interaction(self.block_list[self.num_vertical - 1][self.num_horizontal - 1],
                                             current_filter)


def processing_block(block, current_filter, *args):
    """Handles a block in one iteration."""

    interaction_between_blocks(block, args)
    block.update_data()

    block.color[0] = set_colors(block, current_filter)


def processing_block_without_interaction(block, current_filter):
    """Same as processing_block for blocks that have already been interacted with its neighbours."""

    block.update_data()
    block.color[0] = set_colors(block, current_filter)


def interaction_between_blocks(block, neighbors):
    """Function of Interaction Between Blocks."""

    for neighbor in neighbors:
        water_flow_between_block(block, neighbor)


def water_flow_between_block(block1, block2):
    if block1.height_water > 1 or block2.height_water > 1:
        ground_difference = block1.height_ground - block2.height_ground
        water_difference = block1.height_water - block2.height_water
        difference = ground_difference + water_difference

        if difference > 1 or difference < -1:

            flow = difference * .1

            # if -30 < flow < 30:
            block1.future_height_water -= flow
            block2.future_height_water += flow

            # elif flow > 30:
            #     flow *= .2
            #     block1.future_height_water -= flow
            #     block2.future_height_water += flow
            #
            # elif flow < -30:
            #     flow *= .2
            #     block1.future_height_water -= flow
            #     block2.future_height_water += flow



        # difference = (block1.height_ground + block1.height_water) \
        #              - (block2.height_ground + block2.height_water)
        #
        # flow = difference * 0.2
        # if flow >

        # if difference >= 0:
        #     flow = difference
        #     # flow = difference * 0.2
        #     # if block1.height_water < flow:
        #     #     block1.future_height_water -= block1.height_water
        #     #     block2.future_height_water += block1.height_water
        #
        #     if block1.height_water < flow:
        #         # flow = block1.height_water * 0.2
        #         block1.future_height_water -= flow
        #         block2.future_height_water += flow
        #
        #     else:
        #         block1.future_height_water -= flow
        #         block2.future_height_water += flow
        #
        # if difference < 0:
        #     flow = difference
        #     # flow = (difference ) * 0.2
        #     # if block2.height_water < flow:
        #     #     block2.future_height_water -= block2.height_water
        #     #     block1.future_height_water += block2.height_water
        #
        #     if block1.height_water < flow:
        #         # flow = block1.height_water * 0.2
        #         block1.future_height_water -= flow
        #         block2.future_height_water += flow
        #
        #     else:
        #         block2.future_height_water -= flow
        #         block1.future_height_water += flow


def old_water_flow_between_block(block1, block2):
    difference = (block1.height_ground + block1.height_water) \
                 - (block2.height_ground + block2.height_water)

    if difference > 0:
        flow = difference * 0.2
        if block1.height_water < flow:
            flow = block1.height_water * 0.2
            block1.future_height_water -= flow
            block2.future_height_water += flow

        else:
            block1.future_height_water -= flow
            block2.future_height_water += flow

    if block2.height_water == 0:
        return 0
    else:
        return abs(difference)


def set_colors(block, filter_func):
    """Define colors for all blocks"""

    color = filter_func(block)
    return color

    # def old_iteration(self, color_map, current_filter):
    #     """Calculate all logic contain to world."""
    #
    #     for line in self.block_list:
    #         for block in line:
    #             interaction_between_blocks(block)
    #             block.update_data()
    #
    #             block_color = set_colors(block, current_filter)
    #             color_map.append(block_color)

    # def fibb_main(self):
    #     for number in range(len(self.block_list)):
    #         if number % self.num_horizontal == self.num_horizontal - 1:
    #             dif1 = water_flow_between_block(self.block_list[number], self.block_list[number - self.num_horizontal + 1])
    #             dif2 = water_flow_between_block(self.block_list[number], self.block_list[number - 1])
    #
    #         elif number % self.num_horizontal == 0:
    #             dif1 = water_flow_between_block(self.block_list[number], self.block_list[number + self.num_horizontal - 1])
    #             dif2 = water_flow_between_block(self.block_list[number], self.block_list[number + 1])
    #
    #         else:
    #             dif1 = water_flow_between_block(self.block_list[number], self.block_list[number + 1])
    #             dif2 = water_flow_between_block(self.block_list[number], self.block_list[number - 1])
    #
    #         if 0 <= number <= self.num_horizontal - 1:
    #             dif3 = water_flow_between_block(self.block_list[number], self.block_list[number + self.num_horizontal])
    #             dif4 = dif3
    #
    #         elif len(self.block_list) - self.num_horizontal <= number < len(self.block_list):
    #             dif3 = water_flow_between_block(self.block_list[number], self.block_list[number - self.num_horizontal])
    #             dif4 = dif3
    #
    #         else:
    #             dif3 = water_flow_between_block(self.block_list[number], self.block_list[number + self.num_horizontal])
    #             dif4 = water_flow_between_block(self.block_list[number], self.block_list[number - self.num_horizontal])
    #
    #         self.block_list[number].wave_counter = dif1 + dif2 + dif3 + dif4
