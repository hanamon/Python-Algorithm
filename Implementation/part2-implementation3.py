# 구현 문제 3 : 왕실의 나이트

def alphabet_to_number(str):
    if (str == 'a'): return 1
    elif (str == 'b'): return 2
    elif (str == 'c'): return 3
    elif (str == 'd'): return 4
    elif (str == 'e'): return 5
    elif (str == 'f'): return 6
    elif (str == 'g'): return 7
    elif (str == 'h'): return 8
    else: return int(str)

def action_map(action, position):
    for action in list(action):
        if action == 'U': position[0] -= 1
        elif action == 'D': position[0] += 1
        elif action == 'L': position[1] -= 1
        elif action == 'R': position[1] += 1
    return position

curr_position = list(map(lambda str: alphabet_to_number(str), reversed(input())))
action_list = ['LLU', 'LLD', 'RRU', 'RRD', 'UUL', 'UUR', 'DDL', 'DDR']
map_size = 8
count = 0

for action in action_list:
    result = action_map(action, [curr_position[0], curr_position[1]])
    if (result[0] < 1) | (result[0] > map_size) | (result[1] < 1) | (result[1] > map_size): continue
    count += 1

print(count)