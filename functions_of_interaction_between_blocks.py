def water_flow(block1, block2):
    difference = (block1.height_ground + block1.height_water) - (block2.height_ground + block2.height_water)
    if difference > 0:

