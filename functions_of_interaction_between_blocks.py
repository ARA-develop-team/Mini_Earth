
def water_flow(block1, block2):
    difference = (block1.height_ground + block1.height_water) \
                 - (block2.height_ground + block2.height_water)
    if difference > 0:
        flow = (difference * 20) / 100
        if block1.height_water < flow:
            block2.height_water += block1.height_water
            block1.height_water = 0
        elif flow < 0.01:
            block1.height_water -= difference
        else:
            block1.height_water -= flow
            block2.height_water += flow
    if block2.height_water == 0:
        return 0
    else:
        return abs(difference)

def water_flow_4(block_list, num_horizontal):
    for number in range(len(block_list)):

        if number % num_horizontal == num_horizontal - 1:
            dif1 = water_flow(block_list[number], block_list[number - num_horizontal + 1])
            dif2 =water_flow(block_list[number], block_list[number - 1])
        elif number % num_horizontal == 0:
            dif1 = water_flow(block_list[number], block_list[number + num_horizontal - 1])
            dif2 = water_flow(block_list[number], block_list[number + 1])
        else:
            dif1 = water_flow(block_list[number], block_list[number + 1])
            dif2 = water_flow(block_list[number], block_list[number - 1])

        if 0 <= number <= num_horizontal - 1:
            dif3 = water_flow(block_list[number], block_list[number + num_horizontal])
            dif4 = dif3
        elif len(block_list) - num_horizontal <= number < len(block_list):
            dif3 = water_flow(block_list[number], block_list[number - num_horizontal])
            dif4 = dif3
        else:
            dif3 = water_flow(block_list[number], block_list[number + num_horizontal])
            dif4 = water_flow(block_list[number], block_list[number - num_horizontal])
        block_list[number].wave_counter = dif1 + dif2 + dif3 + dif4
