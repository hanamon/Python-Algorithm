# Part3 그리디 문제 5: 볼링공 고르기

# 둘이 볼링 침
# 서로 무게가 다른 볼링공 고를 것임
# 볼링공 총 N개 있음
# 각 공마다 무게가 적혀있음
# 공 번호는 1부터 순서대로 부여됨 (1부터 M까지의 자연수로 존재함)

n, m = map(int, input().split())
balls = list(map(int, input().split()))
count = 0

for i, currBall in enumerate(balls):
		# print('current index', currBall)
		if i+1 != len(balls):
				for nextBall in balls[i+1:]:
						# print(balls[i+1:], nextBall)
						if currBall != nextBall: count += 1

print(count)

# TODO: DFS로 재귀로 풀이 가능한지