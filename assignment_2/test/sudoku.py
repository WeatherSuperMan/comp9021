from itertools import combinations

class SudokuError(Exception):
    def __init__(self, message):
        self.message = message

class Sudoku:
    def __init__(self, soduku_file):
        self.txt_name = soduku_file
        self.s_str = ''
        self.s_list = list(([None] * 9) for i in range(9))
        self.b_l = list(list(list([''] * 5) for i in range(9)) for j in range(9))
        self.corner_l = list(list(set() for i in range(9)) for j in range(9))
        self.cancel_l = list(list(set() for i in range(9)) for j in range(9))
        i = 0
        j = 0
        k = 0
        with open(self.txt_name) as f:
            for line in f:
                for e in line:
                    
                    if e.isalpha():## include alpha
                        #print(e)
                        raise SudokuError('Incorrect input')
                    
                    if e.isdigit():
                        self.s_str += e
        
        if len(self.s_str) != 81: ## too long or too short
            #print(len(self.s_str))
            raise SudokuError('Incorrect input')
        
        for k in range(len(self.s_str)):
            i = k // 9
            j = k % 9
            self.s_list[i][j] = int(self.s_str[k])




    def preassess(self):
        for i in range(9):## row check
            row_set = set()
            for j in range(9):
                if self.s_list[i][j] in row_set and self.s_list[i][j] != 0:
                    #print('row check', i, j, self.s_list[i][j])
                    print('There is clearly no solution.')
                    return
                else:
                    row_set.add(self.s_list[i][j])
                    
        for k in range(9):## column check
            col_set = set()
            for h in range(9):
                if self.s_list[h][k] in col_set and self.s_list[h][k] != 0:
                    #print('column check', h, k, self.s_list[h][k])
                    print('There is clearly no solution.')
                    return
                else:
                    col_set.add(self.s_list[h][k])

        for r in range(1, 8, 3):## box check
            for s in range(1, 8, 3):
                box_set = set()
                if self.s_list[r][s] in box_set and self.s_list[r][s] != 0:
                    #print('box check', r, s, self.s_list[r][s], box_set)
                    print('There is clearly no solution.')
                    return
                else:
                    box_set.add(self.s_list[r][s])

                if self.s_list[r][s + 1] in box_set and self.s_list[r][s + 1] != 0:
                    #print('box check', r, s + 1, self.s_list[r][s + 1], box_set)
                    print('There is clearly no solution.')
                    return
                else:
                    box_set.add(self.s_list[r][s + 1])

                if self.s_list[r][s - 1] in box_set and self.s_list[r][s - 1] != 0:
                    #print('box check', r, s - 1, self.s_list[r][s - 1], box_set)
                    print('There is clearly no solution.')
                    return
                else:
                    box_set.add(self.s_list[r][s - 1])

                if self.s_list[r + 1][s] in box_set and self.s_list[r + 1][s] != 0:
                    #print('box check', r + 1, s, self.s_list[r + 1][s], box_set)
                    print('There is clearly no solution.')
                    return
                else:
                    box_set.add(self.s_list[r + 1][s])

                if self.s_list[r + 1][s + 1] in box_set and self.s_list[r + 1][s + 1] != 0:
                    #print('box check', r + 1, s + 1, self.s_list[r + 1][s + 1], box_set)
                    print('There is clearly no solution.')
                    return
                else:
                    box_set.add(self.s_list[r + 1][s + 1])

                if self.s_list[r + 1][s - 1] in box_set and self.s_list[r + 1][s - 1] != 0:
                    #print('box check', r + 1, s - 1, self.s_list[r + 1][s - 1], box_set)
                    print('There is clearly no solution.')
                    return
                else:
                    box_set.add(self.s_list[r + 1][s - 1])

                if self.s_list[r - 1][s] in box_set and self.s_list[r - 1][s] != 0:
                    #print('box check', r - 1, s, self.s_list[r - 1][s], box_set)
                    print('There is clearly no solution.')
                    return
                else:
                    box_set.add(self.s_list[r - 1][s])

                if self.s_list[r - 1][s + 1] in box_set and self.s_list[r - 1][s + 1] != 0:
                    #print('box check', r - 1, s + 1, self.s_list[r - 1][s + 1], box_set)
                    print('There is clearly no solution.')
                    return
                else:
                    box_set.add(self.s_list[r - 1][s + 1])

                if self.s_list[r - 1][s - 1] in box_set and self.s_list[r - 1][s - 1] != 0:
                    #print('box check', r - 1, s - 1, self.s_list[r - 1][s - 1], box_set)
                    print('There is clearly no solution.')
                    return
                else:
                    box_set.add(self.s_list[r - 1][s - 1])

        print('There might be a solution.')


    def bare_tex_output(self):
        
        self.b_l = list(list(list([''] * 5) for i in range(9)) for j in range(9))
        
        for i in range(9):
            for j in range(9):
                if self.s_list[i][j] != 0:
                    self.b_l[i][j][4] = self.s_list[i][j]
                    
        self.bare_name = self.txt_name[0 : -4] + '_bare.tex'

        self.create_tex(self.bare_name)
        
            
        #os.system('pdflatex ' + self.bare_name)

        

    def forced_tex_output(self):
        self.b_l = list(list(list([''] * 5) for i in range(9)) for j in range(9))
        self.forced_create()
        
        for i in range(9):
            for j in range(9):
                if self.f_list[i][j] != 0:
                    self.b_l[i][j][4] = self.f_list[i][j]
                    
        self.forced_name = self.txt_name[0 : -4] + '_forced.tex'

        self.create_tex(self.forced_name)
            

    def marked_tex_output(self):
        self.b_l = list(list(list([''] * 5) for i in range(9)) for j in range(9))
        self.marked_create()

        for i in range(9):
            for j in range(9):
                if self.f_list[i][j] != 0:
                    self.b_l[i][j][4] = self.f_list[i][j]

        for i in range(9):
            for j in range(9):
                if self.corner_l[i][j]:
                    for k in range(1, 10):
                        if k in self.corner_l[i][j]:
                            if k == 1 or k == 2:
                                if self.b_l[i][j][0]:
                                    self.b_l[i][j][0] += (' ' + str(k))
                                else:
                                    self.b_l[i][j][0] += str(k)
                            if k == 3 or k == 4:
                                if self.b_l[i][j][1]:
                                    self.b_l[i][j][1] += (' ' + str(k))
                                else:
                                    self.b_l[i][j][1] += str(k)
                            if k == 5 or k == 6:
                                if self.b_l[i][j][2]:
                                    self.b_l[i][j][2] += (' ' + str(k))
                                else:
                                    self.b_l[i][j][2] += str(k)
                            if k == 7 or k == 8 or k == 9:
                                if self.b_l[i][j][3]:
                                    self.b_l[i][j][3] += (' ' + str(k))
                                else:
                                    self.b_l[i][j][3] += str(k)
                                    
        self.marked_name = self.txt_name[0 : -4] + '_marked.tex'

        self.create_tex(self.marked_name)

    def worked_tex_output(self):
        self.b_l = list(list(list([''] * 5) for i in range(9)) for j in range(9))
        self.worked_create()

        for i in range(9):
            for j in range(9):
                if self.f_list[i][j] != 0:
                    self.b_l[i][j][4] = self.f_list[i][j]

                for n in range(1, 3): ## 1, 2
                    if n in self.corner_l[i][j]:
                        if self.b_l[i][j][0]:
                            self.b_l[i][j][0] += (' ' + str(n))
                        else:
                            self.b_l[i][j][0] += str(n)

                    if n in self.cancel_l[i][j]:
                        if self.b_l[i][j][0]:
                            self.b_l[i][j][0] += (' ' + '\\cancel{' + str(n) + '}')
                        else:
                            self.b_l[i][j][0] += ('\\cancel{' + str(n) + '}')
                for n in range(3, 5): ## 3, 4
                    if n in self.corner_l[i][j]:
                        if self.b_l[i][j][1]:
                            self.b_l[i][j][1] += (' ' + str(n))
                        else:
                            self.b_l[i][j][1] += str(n)

                    if n in self.cancel_l[i][j]:
                        if self.b_l[i][j][1]:
                            self.b_l[i][j][1] += (' ' + '\\cancel{' + str(n) + '}')
                        else:
                            self.b_l[i][j][1] += ('\\cancel{' + str(n) + '}')

                for n in range(5, 7): ## 5, 6
                    if n in self.corner_l[i][j]:
                        if self.b_l[i][j][2]:
                            self.b_l[i][j][2] += (' ' + str(n))
                        else:
                            self.b_l[i][j][2] += str(n)

                    if n in self.cancel_l[i][j]:
                        if self.b_l[i][j][2]:
                            self.b_l[i][j][2] += (' ' + '\\cancel{' + str(n) + '}')
                        else:
                            self.b_l[i][j][2] += ('\\cancel{' + str(n) + '}')

                for n in range(7, 10): ## 7, 8, 9
                    if n in self.corner_l[i][j]:
                        if self.b_l[i][j][3]:
                            self.b_l[i][j][3] += (' ' + str(n))
                        else:
                            self.b_l[i][j][3] += str(n)

                    if n in self.cancel_l[i][j]:
                        if self.b_l[i][j][3]:
                            self.b_l[i][j][3] += (' ' + '\\cancel{' + str(n) + '}')
                        else:
                            self.b_l[i][j][3] += ('\\cancel{' + str(n) + '}')
        
        self.worked_name = self.txt_name[0 : -4] + '_worked.tex'

        self.create_tex(self.worked_name)
        
        for line in self.f_list:
            print(line)



    def forced_create(self):
        self.f_list = list(self.s_list)
        box_center = dict({1:(1, 1), 2:(1, 4), 3:(1, 7), 4:(4, 1), 5:(4, 4), 6:(4, 7), 7:(7, 1), 8:(7, 4), 9:(7, 7)})
        
        while(1):
            loop_flag = 0
            most_f_dict = dict({1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0})
            most_f_set = set()

            for i in range(9):
                for j in range(9):
                    if self.f_list[i][j] != 0:
                        most_f_dict[self.f_list[i][j]] += 1

            for key in most_f_dict.keys():
                most_f_set.add(most_f_dict[key])

            while most_f_set: ##频率集合
                max_f = max(most_f_set)
                
                #print('pin lv ji he', most_f_set)
                #print('max pin lv', max_f)
                #print()
                
                for j in range(1, 10):
                    if most_f_dict[j] == max_f: ## 某一数为当前最大频率
                        max_f_num = j
                        
                        #print('dang qian yuan su', max_f_num)
                        #print()
                        
                        for i in range(1, 10): ## box 1 ~ 9
                            x, y = box_center[i]
                            flag_possible = 0
                            if max_f_num not in self.box_set(x, y):
                                #print(i, self.box_set(x, y))
                                #print((x, y), self.f_list[x][y], self.row_set(x, y).union(self.col_set(x, y)), len(self.row_set(x, y).union(self.col_set(x, y))))
                                if self.f_list[x][y] == 0 and max_f_num not in self.row_set(x, y).union(self.col_set(x, y)):
                                    flag_possible += 1
                                    x_possible, y_possible = x, y
                                if self.f_list[x][y - 1] == 0 and max_f_num not in self.row_set(x, y - 1).union(self.col_set(x, y - 1)):
                                    flag_possible += 1
                                    x_possible, y_possible = x, y - 1
                                if self.f_list[x][y + 1] == 0 and max_f_num not in self.row_set(x, y + 1).union(self.col_set(x, y + 1)):
                                    flag_possible += 1
                                    x_possible, y_possible = x, y + 1
                                if self.f_list[x - 1][y] == 0 and max_f_num not in self.row_set(x - 1, y).union(self.col_set(x - 1, y)):
                                    flag_possible += 1
                                    x_possible, y_possible = x - 1, y
                                if self.f_list[x - 1][y - 1] == 0 and max_f_num not in self.row_set(x - 1, y - 1).union(self.col_set(x - 1, y - 1)):
                                    flag_possible += 1
                                    x_possible, y_possible = x - 1, y - 1
                                if self.f_list[x - 1][y + 1] == 0 and max_f_num not in self.row_set(x - 1, y + 1).union(self.col_set(x - 1, y + 1)):
                                    flag_possible += 1
                                    x_possible, y_possible = x - 1, y + 1
                                if self.f_list[x + 1][y] == 0 and max_f_num not in self.row_set(x + 1, y).union(self.col_set(x + 1, y)):
                                    flag_possible += 1
                                    x_possible, y_possible = x + 1, y
                                if self.f_list[x + 1][y - 1] == 0 and max_f_num not in self.row_set(x + 1, y - 1).union(self.col_set(x + 1, y - 1)):
                                    flag_possible += 1
                                    x_possible, y_possible = x + 1, y - 1
                                if self.f_list[x + 1][y + 1] == 0 and max_f_num not in self.row_set(x + 1, y + 1).union(self.col_set(x + 1, y + 1)):
                                    flag_possible += 1
                                    x_possible, y_possible = x + 1, y + 1
                                    

                                if flag_possible == 1:
                                    self.f_list[x_possible][y_possible] = max_f_num
                                    loop_flag = 1
                                    #print('x_possible, y_possible', x_possible, y_possible)

                most_f_set.remove(max_f)
                
            if loop_flag == 0:
                break
            
    def marked_create(self):
        self.forced_create() ## 得到forced list
        self.corner_l = list(list(set() for i in range(9)) for j in range(9))
        box_center = dict({1:(1, 1), 2:(1, 4), 3:(1, 7), 4:(4, 1), 5:(4, 4), 6:(4, 7), 7:(7, 1), 8:(7, 4), 9:(7, 7)})

        for i in range(1, 10): ## box 1 ~ 9
            x, y = box_center[i]
            for n in range(1, 10): ## 数字1 ~ 9
                if n not in self.box_set(x, y):
                    if self.f_list[x][y] == 0 and n not in self.row_set(x, y).union(self.col_set(x, y)):
                        self.corner_l[x][y].add(n)
                    if self.f_list[x][y - 1] == 0 and n not in self.row_set(x, y - 1).union(self.col_set(x, y - 1)):
                        self.corner_l[x][y - 1].add(n)
                    if self.f_list[x][y + 1] == 0 and n not in self.row_set(x, y + 1).union(self.col_set(x, y + 1)):
                        self.corner_l[x][y + 1].add(n)
                    if self.f_list[x - 1][y] == 0 and n not in self.row_set(x - 1, y).union(self.col_set(x - 1, y)):
                        self.corner_l[x - 1][y].add(n)
                    if self.f_list[x - 1][y - 1] == 0 and n not in self.row_set(x - 1, y - 1).union(self.col_set(x - 1, y - 1)):
                        self.corner_l[x - 1][y - 1].add(n)
                    if self.f_list[x - 1][y + 1] == 0 and n not in self.row_set(x - 1, y + 1).union(self.col_set(x - 1, y + 1)):
                        self.corner_l[x - 1][y + 1].add(n)
                    if self.f_list[x + 1][y] == 0 and n not in self.row_set(x + 1, y).union(self.col_set(x + 1, y)):
                        self.corner_l[x + 1][y].add(n)
                    if self.f_list[x + 1][y - 1] == 0 and n not in self.row_set(x + 1, y - 1).union(self.col_set(x + 1, y - 1)):
                        self.corner_l[x + 1][y - 1].add(n)
                    if self.f_list[x + 1][y + 1] == 0 and n not in self.row_set(x + 1, y + 1).union(self.col_set(x + 1, y + 1)):
                        self.corner_l[x + 1][y + 1].add(n)
        
    def worked_create(self):
        self.marked_create() ## 得到forced list， corner list
        self.cancel_l = list(list(set() for i in range(9)) for j in range(9))

        while(1): ## preemptive set check
            a = self.find_single_number()
            b = self.find_singleton()
            
            r_flag = self.row_preemptive_check()   
            c_flag = self.col_preemptive_check()
            b_flag = self.box_preemptive_check()
            

            if a == 0 and b == 0 and r_flag == 0 and c_flag == 0 and b_flag == 0:
                break
            



    def find_single_number(self):
        for i in range(9):
            for j in range(9): ## all dot
                if len(self.corner_l[i][j]) == 1: ## number only have one choice
                    for e in self.corner_l[i][j]:
                        number = e
                    self.deal_number(i, j ,number) ## deal with number
                    #print('find_single_number', (i ,j), number)
                    return 1
        return 0
        
    def find_singleton(self):
        for row in range(9):
            for col in range(9): ## all dots

                for e in self.corner_l[row][col]: ## e : possible number of dot
                    st_flag = 0
                    for j in range(9):
                        if e in self.corner_l[row][j]: ## occur times 
                            st_flag += 1
                    if st_flag == 1: ## if only in row 
                        self.deal_number(row, col ,e)
                        #print('find_singleton_row', (row, col), e)
                        return 1

                    st_flag = 0
                    for i in range(9):
                        if e in self.corner_l[i][col]:
                            st_flag += 1
                    if st_flag == 1:
                        self.deal_number(row, col ,e)
                        #print('find_singleton_col', (row, col), e)
                        return 1

                    st_flag = 0
                    num_box = self.which_box(row, col) ## which box
                    box_dot_list = self.box_dot(num_box) ## box dot list
                    for dot in box_dot_list:
                        x,y = dot
                        if e in self.corner_l[x][y]:
                            st_flag += 1
                    if st_flag == 1:
                        self.deal_number(row, col ,e)
                        #print('find_singleton_box', (row, col), e)
                        return 1

        return 0 



    def deal_number(self, x, y ,number):
        row = x
        col = y
        self.f_list[x][y] = number
        for e in self.corner_l[x][y]:
            self.cancel_l[x][y].add(e)
        self.corner_l[x][y] = set() ## number has been found
        for j in range(9): ## row remove number
            if number in self.corner_l[row][j]:
                self.corner_l[row][j].remove(number)
                self.cancel_l[row][j].add(number)

        for i in range(9): ## row remove number
            if number in self.corner_l[i][col]:
                self.corner_l[i][col].remove(number)
                self.cancel_l[i][col].add(number)

        num_box = self.which_box(x, y)
        box_dot_list = self.box_dot(num_box)
        #print(box_dot_list)
        for e in box_dot_list: ## box remove number
            a, b = e
            if number in self.corner_l[a][b]:
                self.corner_l[a][b].remove(number)
                self.cancel_l[a][b].add(number)


                
            
    def row_preemptive_check(self):
        comb_row = self.get_row_comb()
        r_flag = 0
        ##print(self.get_row_comb())
        if comb_row:
            for size_set in comb_row: ## certain size combination
                for tuple_set in size_set: ## one tuple set
                    if len(tuple_set) < 2:
                        continue
                    number_set = set()
                    size_number_set = 0
                    size_tuple_set = len(tuple_set)
                    
                    for one_tuple in tuple_set: 
                        x, y = one_tuple
                        for num_e in self.corner_l[x][y]:
                            number_set.add(num_e) ## numbers in preemptive set

                    size_number_set = len(number_set)
                    if size_number_set == size_tuple_set: ## if preemptive set exist 
                        row = x
                        row_tuple = self.row_dot(row)
                        #print('row_preemptive_check')
                        #print('row:',row, tuple_set, number_set)
                        #print(row_tuple)
                        for e in row_tuple: ## tuple in that row
                            if e not in tuple_set:
                                e_x, e_y = e
                                do_flag = self.not_in_preemp(e_x, e_y, number_set) ## do function not_in_preemp()
                                r_flag += do_flag 
                                #print(e, do_flag)
                        if r_flag != 0:
                            while(1): ## find_single_number() and find_singleton()
                                a = self.find_single_number()
                                b = self.find_singleton()
                                if a == 0 and b == 0:
                                    break
                            return 1

        return 0
        




    def col_preemptive_check(self):
        comb_col = self.get_col_comb()
        c_flag = 0
        if comb_col:
            for size_set in comb_col: ## certain size combination
                for tuple_set in size_set: ## one tuple set
                    if len(tuple_set) < 2:
                        continue
                    number_set = set()
                    size_number_set = 0
                    size_tuple_set = len(tuple_set)
                    for one_tuple in tuple_set: 
                        x, y = one_tuple
                        for num_e in self.corner_l[x][y]:
                            number_set.add(num_e) ## numbers in preemptive set
                    size_number_set = len(number_set)
                    if size_number_set == size_tuple_set: ## if preemptive set exist 
                        col = y
                        col_tuple = self.col_dot(col)
                        #print('col_preemptive_check')
                        #print('col:',col, tuple_set, number_set)
                        for e in col_tuple: ## tuple in that row
                            if e not in tuple_set:
                                e_x, e_y = e
                                do_flag = self.not_in_preemp(e_x, e_y, number_set) ## do function not_in_preemp()
                                c_flag += do_flag
                                #print(e, do_flag)
                        if c_flag != 0:
                            while(1): ## find_single_number() and find_singleton()
                                a = self.find_single_number()
                                b = self.find_singleton()
                                if a == 0 and b == 0:
                                    break
                            return 1
                                                 
        return 0




    def box_preemptive_check(self):
        comb_box = self.get_box_comb()
        b_flag = 0
        if comb_box:
            for size_set in comb_box: ## certain size combination
                for tuple_set in size_set: ## one tuple set
                    if len(tuple_set) < 2:
                        continue
                    number_set = set()
                    size_number_set = 0
                    size_tuple_set = len(tuple_set)
                    for one_tuple in tuple_set: 
                        x, y = one_tuple
                        for num_e in self.corner_l[x][y]:
                            number_set.add(num_e) ## numbers in preemptive set
                    size_number_set = len(number_set)
                    if size_number_set == size_tuple_set: ## if preemptive set exist 

                        box_num = self.which_box(x, y)
                        box_tuple = self.box_dot(box_num)
                        #print('box_preemptive_check')
                        #print('box:',box_num, tuple_set, number_set)
                        for e in box_tuple: ## tuple in that row
                            if e not in tuple_set:
                                e_x, e_y = e
                                do_flag = self.not_in_preemp(e_x, e_y, number_set) ## do function not_in_preemp()
                                b_flag += do_flag
                                #print(e, do_flag)
                        if b_flag != 0:
                            while(1): ## find_single_number() and find_singleton()
                                a = self.find_single_number()
                                b = self.find_singleton()
                                if a == 0 and b == 0:
                                    break
                            return 1
                                                 
        return 0





    def not_in_preemp(self, x ,y, number_set):
        temp_set = set(self.corner_l[x][y])
        do_times = 0
        for e in temp_set:
            if e in number_set:
                do_times += 1
                self.corner_l[x][y].remove(e)
                self.cancel_l[x][y].add(e)

        return do_times
        
                    


    def get_row_comb(self):
        comb = list()
        for i in range(9): ## row check
            row_dot = set()
            for j in range(9): ## row dot set
                if self.f_list[i][j] == 0:
                    row_dot.add((i, j))
                
            for k in range(2, len(row_dot) + 1): ## possible combinations of dot, size 2 ~ 9, possible_l 0 ~ 7
                comb.append(set(combinations(row_dot, k)))
        return comb



    def get_col_comb(self):
        comb = list()
        for j in range(9): ## col check
            col_dot = set()
            for i in range(9): ## col dot set
                if self.f_list[i][j] == 0:
                    col_dot.add((i, j))

            for k in range(2, len(col_dot) + 1): ## possible combinations of dot, size 2 ~ 9, possible_l 0 ~ 7
                comb.append(set(combinations(col_dot, k)))
        return comb




    def get_box_comb(self):
        comb = list()
        for n in range(1, 10):
            box_dot = set()
            all_box_dot = self.box_dot(n)
            for t in all_box_dot:
                x, y = t
                if self.f_list[x][y] == 0:
                    box_dot.add((x, y))
            
            for k in range(2, len(box_dot) + 1): ## possible combinations of dot, size 2 ~ 9, possible_l 0 ~ 7
                comb.append(set(combinations(box_dot, k)))
        return comb

        

          
    def box_dot(self, n):
        box_center = dict({1:(1, 1), 2:(1, 4), 3:(1, 7), 4:(4, 1), 5:(4, 4), 6:(4, 7), 7:(7, 1), 8:(7, 4), 9:(7, 7)})
        c_dot = box_center[n]
        x, y =  c_dot
        box_dot_list = list([(x - 1, y - 1),(x - 1, y),(x - 1, y + 1),(x, y - 1),(x, y),(x, y + 1),(x + 1, y - 1),(x + 1, y),(x + 1, y + 1)])
        return box_dot_list

    def row_dot(self, r):
        row_dot_list = list([(r, 0),(r, 1),(r, 2),(r, 3),(r, 4),(r, 5),(r, 6),(r, 7),(r, 8)])
        return row_dot_list

    def col_dot(self, c):
        col_dot_list = list([(0, c),(1, c),(2, c),(3, c),(4, c),(5, c),(6, c),(7, c),(8, c)])
        return col_dot_list
    
        
    def which_box(self, x, y):
        if x <= 2:
            if y <= 2:
                return 1
            elif y > 2 and y <= 5:
                return 2
            else:
                return 3
        elif x >2 and x <= 5:
            if y <= 2:
                return 4
            elif y > 2 and y <= 5:
                return 5
            else:
                return 6
        else:
            if y <= 2:
                return 7
            elif y > 2 and y <= 5:
                return 8
            else:
                return 9
        
    
    def box_set(self, x, y):
        box_set = set()
        if self.f_list[x][y] != 0:
            box_set.add(self.f_list[x][y])
        if self.f_list[x][y - 1] != 0:
            box_set.add(self.f_list[x][y - 1])
        if self.f_list[x][y + 1] != 0:
            box_set.add(self.f_list[x][y + 1])
        if self.f_list[x + 1][y] != 0:
            box_set.add(self.f_list[x + 1][y])
        if self.f_list[x + 1][y - 1] != 0:
            box_set.add(self.f_list[x + 1][y - 1])
        if self.f_list[x + 1][y + 1] != 0:
            box_set.add(self.f_list[x + 1][y + 1])
        if self.f_list[x - 1][y] != 0:
            box_set.add(self.f_list[x - 1][y])
        if self.f_list[x - 1][y + 1] != 0:
            box_set.add(self.f_list[x - 1][y + 1])
        if self.f_list[x - 1][y - 1] != 0:
            box_set.add(self.f_list[x - 1][y - 1])
        return box_set
    
    def row_set(self, x, y):
        row_set = set()
        for i in range(9):
            if self.f_list[x][i] != 0:
                row_set.add(self.f_list[x][i])
        return row_set

    def col_set(self, x, y):
        col_set = set()
        for i in range(9):
            if self.f_list[i][y] != 0:
                col_set.add(self.f_list[i][y])
        return col_set
    
    def create_tex(self, name):
        with open(name, 'w') as latex_file:

            print('\\documentclass[10pt]{article}\n'
                  '\\usepackage[left=0pt,right=0pt]{geometry}\n'
                  '\\usepackage{tikz}\n'
                  '\\usetikzlibrary{positioning}\n'
                  '\\usepackage{cancel}\n'
                  '\\pagestyle{empty}\n'
                  '\n'
                  '\\newcommand{\\N}[5]{\\tikz{\\node[label=above left:{\\tiny #1},\n'
                  '                               label=above right:{\\tiny #2},\n'
                  '                               label=below left:{\\tiny #3},\n'
                  '                               label=below right:{\\tiny #4}]{#5};}}\n'
                  '\n'
                  '\\begin{document}\n'
                  '\n'
                  '\\tikzset{every node/.style={minimum size=.5cm}}\n'
                  '\n'
                  '\\begin{center}\n'
                  '\\begin{tabular}{||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||@{}c@{}|@{}c@{}|@{}c@{}||}\\hline\\hline', file = latex_file
                 )

            for n in range(0, 9):## swap in the end
                print(f'% Line {n + 1}\n'
                      '\\N{'f'{self.b_l[n][0][0]}''}{'f'{self.b_l[n][0][1]}''}{'f'{self.b_l[n][0][2]}''}{'f'{self.b_l[n][0][3]}''}{'f'{self.b_l[n][0][4]}'
                      '} & \\N{'f'{self.b_l[n][1][0]}''}{'f'{self.b_l[n][1][1]}''}{'f'{self.b_l[n][1][2]}''}{'f'{self.b_l[n][1][3]}''}{'f'{self.b_l[n][1][4]}'
                      '} & \\N{'f'{self.b_l[n][2][0]}''}{'f'{self.b_l[n][2][1]}''}{'f'{self.b_l[n][2][2]}''}{'f'{self.b_l[n][2][3]}''}{'f'{self.b_l[n][2][4]}''} &\n'
                          
                      '\\N{'f'{self.b_l[n][3][0]}''}{'f'{self.b_l[n][3][1]}''}{'f'{self.b_l[n][3][2]}''}{'f'{self.b_l[n][3][3]}''}{'f'{self.b_l[n][3][4]}'
                      '} & \\N{'f'{self.b_l[n][4][0]}''}{'f'{self.b_l[n][4][1]}''}{'f'{self.b_l[n][4][2]}''}{'f'{self.b_l[n][4][3]}''}{'f'{self.b_l[n][4][4]}'
                      '} & \\N{'f'{self.b_l[n][5][0]}''}{'f'{self.b_l[n][5][1]}''}{'f'{self.b_l[n][5][2]}''}{'f'{self.b_l[n][5][3]}''}{'f'{self.b_l[n][5][4]}''} &\n'
                          
                      '\\N{'f'{self.b_l[n][6][0]}''}{'f'{self.b_l[n][6][1]}''}{'f'{self.b_l[n][6][2]}''}{'f'{self.b_l[n][6][3]}''}{'f'{self.b_l[n][6][4]}'
                      '} & \\N{'f'{self.b_l[n][7][0]}''}{'f'{self.b_l[n][7][1]}''}{'f'{self.b_l[n][7][2]}''}{'f'{self.b_l[n][7][3]}''}{'f'{self.b_l[n][7][4]}'
                      '} & \\N{'f'{self.b_l[n][8][0]}''}{'f'{self.b_l[n][8][1]}''}{'f'{self.b_l[n][8][2]}''}{'f'{self.b_l[n][8][3]}''}{'f'{self.b_l[n][8][4]}''} \\\ \\hline', file = latex_file, end = ''
                      )
                    
                if (n + 1) % 3 == 0:
                    print('\\hline', file = latex_file)
                else:
                    print('', file = latex_file)

                if n != 8:
                    print('', file = latex_file)
            

            print('\\end{tabular}\n'
                  '\\end{center}\n'
                  '\n'
                  '\\end{document}', file = latex_file
                 )
     

    
