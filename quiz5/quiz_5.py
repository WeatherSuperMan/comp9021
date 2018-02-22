# Randomly fills a grid of size height and width whose values are input by the user,
# with nonnegative integers randomly generated up to an upper bound N also input the user,
# and computes, for each n <= N, the number of paths consisting of all integers from 1 up to n
# that cannot be extended to n+1.
# Outputs the number of such paths, when at least one exists.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def get_paths():
    output[1] = 0
    for length in range(1, max_length + 1):
        next_length = length + 1
        last_length = length - 1
        output[length + 1] = 0
        if length == 1:     ##1的路径
            for i in range(height):
                for j in range(width):                    
                    if grid[i][j] == 1:
                        p_flag = 0
                        if j <= width - 2:
                            if grid[i][j + 1] == next_length:       ##与下一级路径相关
                                p_flag += 1
                                output[length + 1] += 1
                                if (i, j + 1) not in dict_point[length + 1]:
                                    dict_point[length + 1].append((i, j + 1))
                                    dict_point_num[(i, j + 1)] = 1  ##存与上一级路径相关联次数
                                else:
                                    dict_point_num[(i, j + 1)] += 1
                        
                        if j >= 1:
                            if grid[i][(j - 1)] == next_length:
                                p_flag += 1
                                output[length + 1] += 1
                                if (i, j - 1) not in dict_point[length + 1]:
                                    dict_point[length + 1].append((i, j - 1))
                                    dict_point_num[(i, j - 1)] = 1
                                else:
                                    dict_point_num[(i, j - 1)] += 1
                        
                        if i <= height - 2:
                            if grid[i + 1][j] == next_length:
                                p_flag += 1
                                output[length + 1] += 1
                                if (i + 1, j) not in dict_point[length + 1]:
                                    dict_point[length + 1].append((i + 1, j))
                                    dict_point_num[(i + 1, j)] = 1
                                else:
                                    dict_point_num[(i + 1, j)] += 1
                                    
                        if i >= 1:
                            if grid[i - 1][j] == next_length:
                                p_flag += 1
                                output[length + 1] += 1
                                if (i - 1, j) not in dict_point[length + 1]:
                                    dict_point[length + 1].append((i - 1, j))
                                    dict_point_num[(i - 1, j)] = 1
                                else:
                                    dict_point_num[(i - 1, j)] += 1
                        if p_flag == 0:
                            output[length] += 1
                                              
        elif length >= 2:
            for (x, y) in dict_point[length]:
                p_flag = 0
                c_flag = 1
                if y <= width - 2:
                    if grid[x][y + 1] == next_length:
                        p_flag += 1
                        output[length + 1] += 1
                        if (x, y + 1) not in dict_point[length + 1]:
                            dict_point[length + 1].append((x, y + 1))
                            dict_point_num[(x, y + 1)] = 0
                        else:
                            dict_point_num[(x, y + 1)] += 1
                            
                if y >= 1:
                    if grid[x][(y - 1)] == next_length:
                        p_flag += 1
                        output[length + 1] += 1
                        if (x, y - 1) not in dict_point[length + 1]:
                            dict_point[length + 1].append((x, y - 1))
                            dict_point_num[(x, y - 1)] = 0
                        else:
                            dict_point_num[(x, y - 1)] += 1
                            
                if x <= height - 2:
                    if grid[x + 1][y] == next_length:
                        p_flag += 1
                        output[length + 1] += 1
                        if (x + 1, y) not in dict_point[length + 1]:
                            dict_point[length + 1].append((x + 1, y))
                            dict_point_num[(x + 1, y)] = 0
                        else:
                            dict_point_num[(x + 1, y)] += 1
                         
                if x >= 1:
                    if grid[x - 1][y] == next_length:
                        p_flag += 1
                        output[length + 1] += 1
                        if (x - 1, y) not in dict_point[length + 1]:
                            dict_point[length + 1].append((x - 1, y))
                            dict_point_num[(x - 1, y)] = 0
                        else:
                            dict_point_num[(x - 1, y)] += 1

                if p_flag != 0:     ##如果与下一级路径相关
                    output[length] -= dict_point_num[(x, y)]  ##本级路径数减去与上一级路径相关联次数

                
        if output[length] == 0:     ##去掉数量为零的路径
            output.pop(length)
                
    output.pop(max_length + 1)      ##去掉最后一次生成的不必要路径
    return output
                                  
dict_num = defaultdict()
dict_point = defaultdict(list)
dict_point_num = defaultdict()
output = defaultdict()
    
try:
    for_seed, max_length, height, width = [int(i) for i in
                                                  input('Enter four nonnegative integers: ').split()
                                       ]
    if for_seed < 0 or max_length < 0 or height < 0 or width < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randint(0, max_length) for _ in range(width)] for _ in range(height)]
print('Here is the grid that has been generated:')
display_grid()
paths = get_paths()
if paths:
    for length in sorted(paths):
        print(f'The number of paths from 1 to {length} is: {paths[length]}')
