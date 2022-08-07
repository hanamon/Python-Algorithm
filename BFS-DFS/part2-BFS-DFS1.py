# BFS/DFS 문제 1 : 음료수 얼려 먹기

# N x M 크기의 얼음 틀이 있다.
# 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
# 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하라.

# 입력 조건 1: 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다. (1 <= N, M <= 1,000) 
# 입력 조건 2: 두 번째 줄부터 N+1 번째 줄까지 얼음 틀의 형태가 주어진다.
# 입력 조건 3: 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.
# 출력 조건: 한 번에 만들 수 있는 아이스크림의 개수를 출력한다.

# 입력: 여기에서는 입력값을 2차원 배열로 쉽게 표현하였다.
inp = [
  [0,0,1,1,0], 
  [0,0,0,1,1], 
  [1,1,1,1,1], 
  [0,0,0,0,0]
]

# [구현 방법]
# 최단 거리를 구하는 문제이므로 BFS로 구현한다.
# BFS이니 자료구조 Queue를 이용한다.

def my_solution(matrix):
		matrix = [i for i in matrix]
		n, m =  len(matrix)-1, len(matrix[0])-1
		y, x = 0, 0
		count = 0

		for row_idx, row in enumerate(matrix):
				for col_idx, col in enumerate(row):
						if col == 1: continue

						# 아이스크림 블럭을 카운트한다.
						count += 1

						# 다음에 방문할 노드를 큐에 담는다.
						queue = [[row_idx, col_idx]]

						# 현재 아이스크림 블럭과 연결된 블럭을 찾는다.
						while len(queue):
								[y, x] = queue.pop(0)

								# 행렬을 벗어났거나 1인 경우
								if y < 0 or y > n or x < 0 or x > m: continue
								if matrix[y][x] == 1: continue

								# 0인 경우 1로 변경한다.
								matrix[y][x] = 1

								# 상, 하, 좌, 우 검사
								queue.append([y-1, y])
								queue.append([y+1, y])	
								queue.append([y, x-1])
								queue.append([y, x+1])

		return count

print(my_solution(inp))