from random import randint

# Insert your code here
import sys
from random import randint

dice_value = ['Ace', 'King', 'Queen', 'Jack', '10', '9']
result_type = ['Full house', 'One pair', 'Two pair', 'Three of a kind', 'Four of a kind', 'Five of a kind', 'Straight', 'Bust']

type_5 = [0, 0, 0, 0, 0, 5]
type_4 = [0, 0, 0, 0, 1, 4]
type_3 = [0, 0, 0, 1, 1, 3]
type_2 = [0, 0, 0, 1, 2, 2]
type_1 = [0, 0, 1, 1, 1, 2]
full_type = [0, 0, 0, 0, 2, 3]

def play():
    hand_dict = dict({'Ace':0, 'King':0, 'Queen':0, 'Jack':0, '10':0, '9':0})
    for i in range(3):
        hand_list = []
        hand_num = 0
        for key in hand_dict.keys():
            hand_num += hand_dict[key]##判断手牌数量
        for j in range(5 - hand_num):
            hand_dict[dice_value[randint(0, 5)]] += 1##补充手牌到5张，记录到hand_dict
        
        for key in hand_dict.keys():
            if hand_dict[key] != 0:
                for k in range(hand_dict[key]):
                    hand_list.append(key)##将hand_dict内手牌记录到hand_list中
        print(f'The roll is: {hand_list[0]} {hand_list[1]} {hand_list[2]} {hand_list[3]} {hand_list[4]}')

        type_flag = 0
        type_list = []
        
        for key in hand_dict.keys():
            type_list.append(hand_dict[key])##将牌数存入type_list
        type_list.sort()##排序以便判断

        if type_list == type_5:
            type_flag = 5
        elif type_list == type_4:
            type_flag = 4
        elif type_list == type_3:
            type_flag = 3
        elif type_list == type_2:
            type_flag = 2
        elif type_list == type_1:
            type_flag = 1
        elif type_list == full_type:
            type_flag = 0
        else:
            if hand_dict['Ace'] == 0 or hand_dict['9'] == 0:
                type_flag = 6
            else:
                type_flag = 7

        print(f'It is a {result_type[type_flag]}')

        if i < 2:##玩3次，最多换2次牌
            while True:
                roll_times = str()
                if i == 0:
                    roll_times = 'second'##roll次数
                else:
                    roll_times = 'third'
                keep_hand_dict = dict({'Ace':0, 'King':0, 'Queen':0, 'Jack':0, '10':0, '9':0})##初始化保存的手牌
                try:
                    keep_string = input(f'Which dice do you want to keep for the {roll_times} roll? ')##用户输入
                except ValueError:
                    pass

                try:
                    keep_card = keep_string.split()##将输入字符串按空格分割，并存入keep_card，变成list
                    if len(keep_card) == 1 and (keep_card[0] == 'all' or keep_card[0] == 'All'):##如果留牌为all或All，不再换牌退出程序
                        print('Ok, done.')
                        return
                    
                    elif len(keep_card) <= 5 and len(keep_card) >= 0:##如果留牌0到5张
                        if len(keep_card) == 0:##如果输入字符串为空，手牌清零并break
                            hand_dict = dict({'Ace':0, 'King':0, 'Queen':0, 'Jack':0, '10':0, '9':0})
                            break
                        else:##如果keep_card里有1到5个字符串
                            for e in keep_card:
                                if e in dice_value:
                                    keep_hand_dict[e] += 1##如果字符串是牌，该牌留牌数加1
                                else:
                                    raise ValueError##如果字符串不是牌，报错
                            if keep_hand_dict == hand_dict:##如果留牌等于手牌，不再换牌退出程序
                                print('Ok, done.')
                                return
                            else:
                                for key in keep_hand_dict.keys():
                                    if keep_hand_dict[key] <= hand_dict[key]:##如果每张牌留牌数在手牌数量之内，pass
                                        pass
                                    else:##如果有牌的留牌数大于手牌数，报错
                                        raise ValueError
                                hand_dict = dict(keep_hand_dict)##如果留牌数正确，手牌换成留牌
                                break
                    else:##如果字符串数量大于手牌数，报错
                        raise ValueError
                except ValueError:
                    print('That is not possible, try again!')


                    
def simulate(test_time):
    test_result = [0 ,0, 0, 0, 0, 0, 0]
    test_ratio = [0 ,0, 0, 0, 0, 0, 0]
    if test_time == 0:
        pass
    else:
        for i in range(test_time):
            hand_dict = dict({'Ace':0, 'King':0, 'Queen':0, 'Jack':0, '10':0, '9':0})
            for j in range(5):##roll牌
                hand_dict[dice_value[randint(0, 5)]] += 1

            type_list = []
            for key in hand_dict.keys():
                type_list.append(hand_dict[key])##将牌数存入type_list
            type_list.sort()##排序以便判断

            if type_list == type_5:##判断type
                test_result[0] += 1
            elif type_list == type_4:
                test_result[1] += 1
            elif type_list == type_3:
                test_result[4] += 1
            elif type_list == type_2:
                test_result[5] += 1
            elif type_list == type_1:
                test_result[6] += 1
            elif type_list == full_type:
                test_result[2] += 1
            else:
                if hand_dict['Ace'] == 0 or hand_dict['9'] == 0:
                    test_result[3] += 1
                else:
                    pass

        for k in range(len(test_result)):
            test_ratio[k] = format((test_result[k] / test_time) * 100,'.2f')##算出百分比


        
    print(f'Five of a kind : {test_ratio[0]}%')
    print(f'Four of a kind : {test_ratio[1]}%')
    print(f'Full house     : {test_ratio[2]}%')
    print(f'Straight       : {test_ratio[3]}%')
    print(f'Three of a kind: {test_ratio[4]}%')
    print(f'Two pair       : {test_ratio[5]}%')
    print(f'One pair       : {test_ratio[6]}%')


