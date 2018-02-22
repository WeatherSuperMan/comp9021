# Creates a class to represent a permutation of 1, 2, ..., n for some n >= 0.
#
# An object is created by passing as argument to the class name:
# - either no argument, in which case the empty permutation is created, or
# - "length = n" for some n >= 0, in which case the identity over 1, ..., n is created, or
# - the numbers 1, 2, ..., n for some n >= 0, in some order, possibly together with "lengh = n".
#
# __len__(), __repr__() and __str__() are implemented, the latter providing the standard form
# decomposition of the permutation into cycles (see wikepedia page on permutations for details).
#
# Objects have:
# - nb_of_cycles as an attribute
# - inverse() as a method
#
# The * operator is implemented for permutation composition, for both infix and in-place uses.
#
# Written by *** and Eric Martin for COMP9021


class PermutationError(Exception):
    def __init__(self, message):
        self.message = message

class Permutation:
        
    def __init__(self, *args, length = None):


        for i in range(0, len(args)):##args里是int型
            if not isinstance(args[i], int):
                raise PermutationError('Cannot generate permutation from these arguments')
            
        if len(args) != 0:##获取标准格式
            standard_set = {j for j in range(1, max(args) + 1)}
        args_set = set(args)
        
        if len(args) == 0 and length == None:##either no argument, in which case the empty permutation is created
            self.tuple = args

        elif len(args) == 0 and length != None and length > 0:##"length = n" for some n >= 0, in which case the identity over 1, ..., n is created
            self.tuple = tuple(j for j in range(1, length + 1))
            

        elif len(args) > 0 and ((length != None and length == len(args_set)) or (length == None)) \
             and args_set == standard_set:
                                ## the numbers 1, 2, ..., n for some n >= 0, in some order, possibly together with "lengh = n".
            self.tuple = args

        else:
            raise PermutationError('Cannot generate permutation from these arguments')

        from collections import defaultdict
        self.dict = defaultdict()
        for k in range(len(self.tuple)):
            self.dict[k + 1] = self.tuple[k]##建好字典

        temp_list = list()    
        self.circle_list = list(list())
        used_set = set()##把形成的cycle并入set中

        if len(self.dict) == 0:
            pass
        else:
            key = 1
            temp_list.append(1)
            used_set = used_set.union({1})
            while True:##寻找circle
                if self.dict[key] != temp_list[0]:
                    temp_list.append(self.dict[key])
                    key = self.dict[key]
                else:
                    self.circle_list.append(temp_list)
                    used_set = used_set.union(set(temp_list))
                    temp_list = list()
                    for key_ in self.dict.keys():
                        if key_ not in used_set:
                            key = key_
                            temp_list.append(key)
                            break

                if len(used_set) == len(self.dict):
                    break

        for i in range(len(self.circle_list)):##重新排列数组
            self.circle_list[i] = self.circle_list[i][self.circle_list[i].index(max(self.circle_list[i])) : ] + \
                             self.circle_list[i][0 : self.circle_list[i].index(max(self.circle_list[i]))]
        self.circle_list.sort(key = lambda x:x[0])##x为第一维，x[0]为第二维第1位

        self.nb_of_cycles = len(self.circle_list)##cycle数量
        
    def __len__(self):
        return len(self.tuple)##返回长度

    def __repr__(self):
        return f'Permutation{self.tuple}'##print自身

    def __str__(self):
        l = ''
        if len(self.circle_list) == 0:
            l = '()'
        else:
            for i in range(len(self.circle_list)):##按格式输出
                l += '('
                for j in range(len(self.circle_list[i])):
                    l += str(self.circle_list[i][j])
                    if j != len(self.circle_list[i]) - 1:
                        l += ' '
                l += ')'
        return f'{l}'
    
    
    def __mul__(self, permutation):
        mul_list = list()
        if len(self.dict) == len(permutation.dict) != 0:
            for key in self.dict.keys():
                mul_list.append(permutation.dict[self.dict[key]])
            mul_tuple = tuple(mul_list)
            return Permutation(*mul_tuple)
        elif len(self.dict) != len(permutation.dict):
            raise PermutationError('Cannot compose permutations of different lengths')
        else:
            return Permutation()
        
    def __imul__(self, permutation):
        imul_list = list()
        if len(self.dict) == len(permutation.dict) != 0:
            for key in self.dict.keys():
                imul_list.append(permutation.dict[self.dict[key]])
            imul_tuple = tuple(imul_list)
            return Permutation(*imul_tuple)
        elif len(self.dict) != len(permutation.dict):
            raise PermutationError('Cannot compose permutations of different lengths')
        else:
            return Permutation()
        
    def inverse(self):
        l = []
        if len(self.dict) != 0:
            for i in range(len(self.dict)):
                for key in self.dict.keys():
                    if self.dict[key] == i + 1:
                        l.append(key)
                        break              
        inv = tuple(l)       
        return Permutation(*inv)##返回什么
        

                
        
