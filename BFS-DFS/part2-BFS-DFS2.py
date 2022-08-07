# BFS/DFS 문제 2 : 미로 탈출

# 하나몬은 N x M 크기의 직사각형 형태의 미로에 갇혀있다.
# 미로에는 여러 먀래의 괴물이 있어 피해서 탈출해야 한다.
# 하나몬의 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재한다.
# 한 번에 한 칸씩 이동할 수 있다.
# 이 때 괴물이 있는 부분은 0이고, 괴물이 없는 부분은 1로 표시되어 있다.
# 미로는 반드시 탈출할 수 있는 형태로 제시된다.
# 이 때 하나몬이 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하라.
# 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

# 입력 조건 : 첫째 줄에 두 정수 N, M(4 <= N, M <= 200)이 주어진다.
# 입력 조건 : 다음 N개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어진다.
# 입력 조건 : 각가의 수들은 공백 없이 붙어서 입력으로 제시된다.
# 입력 조건 : 시작 칸과 마지막 칸은 항상 1이다.
# 출력 조건 : 첫째 줄에 최소 이동 카의 개수를 출력한다.

# 입력: 여기에서는 입력값을 2차원 배열로 쉽게 표현하였다.
inp = [
  [1,0,1,0,1,0],
  [1,1,1,1,1,1],
  [0,0,0,0,0,1],
  [1,1,1,1,1,1],
  [1,1,1,1,1,1]
]

# [구현 방법]
# 최단 거리를 구하는 문제이므로 BFS로 구현한다.
# BFS이니 자료구조 Queue를 이용한다.

def my_solution(matrix):
		matrix = [i for i in matrix]
		n, m = len(matrix)-1, len(matrix[0])-1
		queue = [[0, 0, 1]] # 배열 순서대로 y, x, count를 의미한다.

		while len(queue):
				[y, x, count] = queue.pop(0)
    
				# 행렬을 벗어났거나 괴물을 만난 경우
				if y < 0 or y > n or x < 0 or x > m: continue
				if matrix[y][x] == 0: continue
    
				# 탈출 성공
				if y == n and x == m: return count
    
				# 나자신 초기화
				matrix[y][x] = 0
    
				queue.append([y-1, x, count+1])
				queue.append([y+1, x, count+1])
				queue.append([y, x-1, count+1])
				queue.append([y, x+1, count+1])

print(my_solution(inp))