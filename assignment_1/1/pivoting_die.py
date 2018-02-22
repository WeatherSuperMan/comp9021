#assignment 1 task 1
import sys

while True:
    #input number
    try:
        num = input('Enter the desired goal cell number: ')
    except ValueError:
        print('Incorrect value, try again')
    try:
        num = int(num)
        if num <= 0:
            raise ValueError
        else:
            break
    except ValueError:
        print('Incorrect value, try again')


#define die dict
die = {'top':3,'front':2,'right':1,'bottom':4,'back':5,'left':6}

def action_right():
    global die
    d = dict(die)
    die['right'] = d['top']
    die['top'] = d['left']
    die['left'] = d['bottom']
    die['bottom'] = d['right']

def action_left():
    global die
    d = dict(die)
    die['right'] = d['bottom']
    die['top'] = d['right']
    die['left'] = d['top']
    die['bottom'] = d['left']

def action_forward():
    global die
    d = dict(die)
    die['front'] = d['top']
    die['top'] = d['back']
    die['back'] = d['bottom']
    die['bottom'] = d['front']

def action_back():
    global die
    d = dict(die)
    die['front'] = d['bottom']
    die['top'] = d['front']
    die['back'] = d['top']
    die['bottom'] = d['back']

def action(step_number):
    global action_flag
    global action_counter
    global cell_counter
    action_flag = action_counter % 4
    if action_flag == 0:
        for j in range(step_number):
            action_right() 
        cell_counter += step
        action_counter += 1
    elif action_flag == 1:
        for j in range(step_number):
            action_forward()
        cell_counter += step
        action_counter += 1
    elif action_flag == 2:
        for j in range(step_number):
            action_left()
        cell_counter += step
        action_counter += 1
    elif action_flag == 3:
        for j in range(step_number):
            action_back()
        cell_counter += step
        action_counter += 1

###cell action
if num == 1:
    pass
else:
    action_flag = 0
    action_counter = 0
    cell_counter = 1
    for step in range(1, num):
        for i in range(2):
            if (cell_counter + step) <= num:
                action(step)
            else:
                action(num - cell_counter)
            if cell_counter == num:
                break
        if cell_counter == num:
            break

###out put
print(f'On cell {num},',die['top'],'is at the top,',die['front'],'at the front, and',die['right'],'on the right.')
