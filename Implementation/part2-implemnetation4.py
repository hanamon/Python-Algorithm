# 구현 문제 4 : 게임 개발

# 0: 북,  1: 동, 2: 남, 3: 서
# 0: 육지, 1: 바다
# 캐릭터가 방문한 칸의 수는?
# 네 방향 이미 가본 칸이거나 바다로 되어 있는 칸인 경우,
# 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
# 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
n, m = map(int, input().split())
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_list():
    global direction
    direction -= 1
    if direction == - 1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_list()
    nx = x + dx[direction]
    ny = y + dx[direction]
    
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dx[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        
        turn_time = 0

print(count)