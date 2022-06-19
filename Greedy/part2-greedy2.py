# 그리디 문제 2 : 큰 수의 법칙

# n = 5, m = 8, k = 3
# data = 2 4 5 4 6
# result = 46

# 입력 값 중에 가장 큰 수와 두 번째로 큰 수만 찾아보자.
# 그리고 그 것들을 K번씩 반복해서 M만큼 너하면 된다.

# # N, M, K를 공백으로 구분하여 입력받기
# n, m, k = map(int, input().split())
# print('NMK:', n, m, k)
# # N개의 수를 공백으로 구분하여 입력받기
# data = list(map(int, input().split()))
# print('data:', data)

# data.sort() # 입력받은 수를 정렬하기
# first = data[n - 1] # 가장 큰 수
# second = data[n - 2] # 두 번째로 큰 수

# result = 0

# while True:	
#     for i in range(k): # 가장 큰 수를 K번 더하기 (range 내장 함수는 0 부터 k 까지의 리스트를 만든다.)
#         if m == 0: break # m이 0이라면 반복문 탈출  
#         result += first
#         m -= 1 # 더할 때마다 1씩 빼기
		
#     if m == 0: break # m이 0이라면 반복문 탈출
#     result += second # 두 번째로 큰 수를 한 번 더하기
#     m -= 1 # 더할 때마다 1씩 빼기

# print(result)

#-----------------------------------------------------------#

# 관찰 결과:
# 
# frist가 K만큼 돌 때 second는 한 번 돈다. (딱 떨어지는 경우)
# 즉 K + 1 씩 반복된다.
#
# K + 1 이 몇 번 반복될까?
# M을 (K + 1)로 나눈 만큼 반복된다.
# M이 8이고 K가 3인 경우
# 8 / (3 + 1) = 2 즉, 2번 반복된다. {6, 6, 6, 5} * 2
# 
# 이제 최대값이 더해지는 횟수를 구할 수 있다.
# 모음이 두 번 반복될 때 최대값은 한 모음에 K번 반복됨으로 아래와 같다.
# 최대값 더해지는 횟수 = (M / (K + 1)) * K

# 그런데 M이 (K + 1)에 나누어 떨어지지 않을 경우 고려해야한다.
# (M % (K + 1))을 추가로 더해주어야한다.
# 최대값 더해지는 횟수 = (M / (K + 1)) * K + (M % (K + 1))

# 이제 더해지는 값을 구할 수 있다.
# 최댓값을 몇 번 반복하는지 구한다. => count
# 두 번째 큰 수를 몇번 더할까 > M에 count 만큼 뺀 값 만큼

# 최댓값 더해진 값 = (M / (K + 1)) * K + (M % (K + 1)) * 최댓값
# 두 번째 더해진 값 = (M - 최대값이 더해지는 횟수) * 두 번째 큰 수

#-----------------------------------------------------------#

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)