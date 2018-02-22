import sys
import os

#input
try:
    string = input('Enter between 3 and 10 lowercase letters: ')
except ValueError:
    print('Incorrect input, giving up...')
    sys.exit()

try:
    lowercase = []
    for c in string:
        if c.isspace():
            pass
        elif c.islower():
            lowercase.append(c)
        else:
            raise ValueError
    if len(lowercase) < 3 or len(lowercase) > 10:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up...')
    sys.exit()
    
#define output
highest_score = 0
highest_words = []

#main
satisfied_list = []
lowercase_dict = dict({'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0})
value = dict({'a':2,'b':5,'c':4,'d':4,'e':1,'f':6,'g':5,'h':5,'i':1,'j':7,'k':6,'l':3,'m':5,'n':2,'o':3,'p':5,'q':7,'r':2,'s':1,'t':2,'u':4,'v':6,'w':6,'x':7,'y':5,'z':7})

for e in lowercase:
    lowercase_dict[e] += 1

with open('wordsEn.txt') as f:
    for word in f:##取出每一行作为word
        word_dict = dict({'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0})
        for c in word:
            if c.islower():
                word_dict[c] += 1##记录每个字母个数
        k_flag = 0
        for key in word_dict.keys():
            if word_dict[key] <= lowercase_dict[key]:##确定由输入字母组成
                pass
            else:
                k_flag = 1
                break

        if k_flag == 0:
            word_value = 0
            for key in word_dict.keys():
                word_value += word_dict[key] * value[key]##算出word的value
            satisfied_list.append((word, word_value))##将word与value存入list
        else:
            pass

satisfied_list.sort(key = lambda x:-x[1])##按value从大到小排序
if len(satisfied_list) > 0:##satisfied_list不为空
    highest_score = satisfied_list[0][1]##最大score
    highest_words.append(satisfied_list[0][0])##最大score的word
    for i in range(1, len(satisfied_list)):
        if satisfied_list[i][1] == satisfied_list[0][1]:
            highest_words.append(satisfied_list[i][0])##append相同score的word
        else:
            pass
    highest_words.sort(key = lambda x:(-len(x), x))##字符串长度优先排序，字符大小其次


#output
if len(highest_words) == 0:
    print('No word is built from some of those letters.')
else:
    print(f'The highest score is {highest_score}.')
    if len(highest_words) == 1:
        print(f'The highest scoring word is {highest_words[0]}',end = '')
    else:
        print('The highest scoring words are, in alphabetical order:')
        for e in highest_words:
            print(f'    {e}', end = '')##word里自带\n换行
