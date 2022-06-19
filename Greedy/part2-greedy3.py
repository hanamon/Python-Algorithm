# 그리디 문제 3 : 숫자 카드 게임

# N과 M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
print('n, m:', n, m) # 행열 크기

result = 0

# 한 줄씩 입력받아 확인
for i in range(n):
		data = list(map(int, input().split()))
		# 현재 줄에서 '가장 작은 수' 찾기
		min_value = min(data)
		# '가장 작은 수'들 중에서 가장 큰 수 찾기
		result = max(result, min_value)

print(result)

# 관찰 결과
# 한 행에 가장 작은 수를 찾고
# 각 행의 가장 작은 수중 가장 큰 수를 찾으면 되는 문제이다.