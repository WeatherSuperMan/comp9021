from itertools import combinations

for i in range(9): ## row check
    row_dot = set()
    possible_l = list()
    row_flag = 0
    for j in range(9):
            row_dot.add((i, j))
    print(row_dot)
    print()
    possible_l.append(set(combinations(row_dot, 2)))
    print(possible_l)
    ##for k in range(2, len(row_dot) + 1): ## size 2 ~ 9, possible_l 0 ~ 7
        ##possible_l.add(set(combinations(row_dot, k)))
