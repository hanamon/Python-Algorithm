# 구현 문제 1 : 상하좌우

map_size = int(input())
move_list = list(input().split())
curr_position = [1, 1]

def action_map(action, position):
    if action == 'U': position[0] -= 1
    elif action == 'D': position[0] += 1
    elif action == 'L': position[1] -= 1
    elif action == 'R': position[1] += 1
    return position

for action in move_list:
    result = action_map(action, [curr_position[0], curr_position[1]])
    if (result[0] < 1) | (result[0] > map_size) | (result[1] < 1) | (result[1] > map_size): continue
    curr_position = result

print(curr_position[0], curr_position[1])