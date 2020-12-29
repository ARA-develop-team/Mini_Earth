
def water_flow(block1, block2):
    if block1.height_ground + block1.height_water > \
        block2.height_ground + block2.height_water:
        difference = (block1.height_ground + block1.height_water)\
                     - (block2.height_ground + block2.height_water)
        flow = (difference * 20) / 100
        #if flow < 0.001:
        #    block2.height_water = block1.height_ground + block1.height_water - block2.height_ground
        if block1.height_water < flow:
            block2.height_water += block1.height_water
            block1.height_water = 0
        else:
            block1.height_water -= flow
            block2.height_water += flow


def water_flow_4(block_list, num_horizontal):
    for number in range(len(block_list)):

        if number % num_horizontal == num_horizontal - 1:
            water_flow(block_list[number], block_list[number - num_horizontal + 1])
            water_flow(block_list[number], block_list[number - 1])
        elif number % num_horizontal == 0:
            water_flow(block_list[number], block_list[number + num_horizontal - 1])
            water_flow(block_list[number], block_list[number + 1])
        else:
            water_flow(block_list[number], block_list[number + 1])
            water_flow(block_list[number], block_list[number - 1])

        if 0 <= number <= num_horizontal - 1:
            water_flow(block_list[number], block_list[number + num_horizontal])
        elif len(block_list) - num_horizontal <= number < len(block_list):
            water_flow(block_list[number], block_list[number - num_horizontal])
        else:
            water_flow(block_list[number], block_list[number + num_horizontal])
            water_flow(block_list[number], block_list[number - num_horizontal])