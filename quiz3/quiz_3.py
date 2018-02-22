            # Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and finds out, for given step_number >= 1
# and step_size >= 2, the number of stairs of step_number many steps,
# with all steps of size step_size.
#
# A stair of 1 step of size 2 is of the form
# 1 1
#   1 1
#
# A stair of 2 steps of size 2 is of the form
# 1 1
#   1 1
#     1 1
#
# A stair of 1 step of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#
# A stair of 2 steps of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#         1
#         1 1 1
#
# The output lists the number of stairs from smallest step sizes to largest step sizes,
# and for a given step size, from stairs with the smallest number of steps to stairs
# with the largest number of stairs.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))

def stairs_in_grid():
    
    #create defaultdict d
    d = defaultdict(dict)
    
    #max of size of stair, depending on dim being even or odd
    if dim % 2:
        m_size = (dim + 1) // 2
    else:
        m_size = dim // 2
    
    #figure out dictionary d
    for size in range(m_size, 1, -1):#from largest size to 2
        used_spots = []#record used spots in every loop in a certain size of stair
        for i in range(dim):#every spot in grid
            for j in range(dim):
                first_size_flag = 0
                
                if (i,j) not in used_spots:#check if spot used
                    if (i <= dim - 1) & (j + size - 1 <= dim - 1):
                        for size_ in range(size):#if first line == 1
                            if grid[i][j + size_] >= 1:
                                first_size_flag += 1
                            else:
                                break
                        
                    if first_size_flag == size:#if following steps ==1
                        x = i
                        y = j
                        step_counter = 0
                        while (x + size - 1 <= dim - 1) & (y + 2*size - 2 <= dim - 1):
                            mid_e_flag = 0
                            step_size_flag = 0
                            for mid_e in range(1, size - 1):#check mid elements
                                if grid[x + mid_e][y + size - 1] >= 1:
                                    mid_e_flag += 1
                                else:
                                    break
                            for next_step in range(size):#check next step
                                if grid[x + size - 1][y + size - 1 + next_step] >= 1:
                                    step_size_flag += 1
                                else:
                                    break
                            if (mid_e_flag == size - 2) & (step_size_flag == size):
                                step_counter += 1
                                used_spots.append((x + (size - 1), y + (size - 1)))
                            else:
                                break
                            x += (size - 1)
                            y += (size - 1)
                        if step_counter != 0:
                            if step_counter not in d[size].keys():
                                d[size].update({step_counter:1})
                            else:
                                d[size][step_counter] += 1
                            ##
                            print(size,(i,j),step_counter)
                            ##
                            
    stairs = defaultdict(list)#create stairs
    for num_size in d:
        for num_step in d[num_size]:
            stairs[num_size].append((num_step, d[num_size][num_step]))
    
    for e in stairs:#sort according to steps
        stairs[e].sort()

    ##        
    print(stairs)
    ##
    return (stairs)
    # Replace return {} above with your code

# Possibly define other functions

try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
# A dictionary whose keys are step sizes, and whose values are pairs of the form
# (number_of_steps, number_of_stairs_with_that_number_of_steps_of_that_step_size),
# ordered from smallest to largest number_of_steps.
stairs = stairs_in_grid()
for step_size in sorted(stairs):
    print(f'\nFor steps of size {step_size}, we have:')
    for nb_of_steps, nb_of_stairs in stairs[step_size]:
        stair_or_stairs = 'stair' if nb_of_stairs == 1 else 'stairs'
        step_or_steps = 'step' if nb_of_steps == 1 else 'steps'
        print(f'     {nb_of_stairs} {stair_or_stairs} with {nb_of_steps} {step_or_steps}')
