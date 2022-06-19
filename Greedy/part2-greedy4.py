# 그리디 문제 4 : 1이 될 때까지

# n, k = map(int, input().split())
# step = 0
# count = 0

# while True:
# 		step += 1

# 		if n == 1: break
  
# 		if n % k == 0: n //= k
# 		else: n -= 1

# 		count += 1
  
# print(step)
# print(count)

#-----------------------------------------------------------#

# 왜 풀이가 위의 것보다 복잡하지??
# 입력 값 100억 이상이면 위 식이 무리인가??
# 일일이 1씩 빼는 것이 문제인가??
# N이 K의 배수가 되도록 한 번에 빼야한다??

n, k = map(int, input().split())
step = 0
count = 0

while True:
		step += 1 # 3번 안에 끝남
   
		target = (n // k) * k # 25 // 3 * 3 = 24 (k로 나눌 수 있는 값으로 바꾼다.) =next=> 8 // 3 * 3 = 6 =next=> 2 // 3 * 3 = 0
		count += (n - target) # 25 - 24 = 1 (1을 몇번 빼야 그렇게 되는가? => -1 빼기를 한번에 한다.) =next=> 2 + 8 - 6 = 4 (여기서 -2를 해주면 되는 구나) =next=> 5 + 2 - 0 = 7
		n = target # 24 (나머지를 k로 나누면 된다.) =next=> 6 =next=> n = 0
  
		if n < k: break
  
		count += 1 # 1 + 1  = 2 (딱떨어지게 K를 나눌 때 카운트 해야하죠 + 1) =next=> 4 + 1 = 5
		n //= k # 24 // 3 = 8 (이제 한 번만 더 나누면 되겠네?) =next=> 6 // 3 = 2

print(step)
print(count)

# 관찰 결과
# 위와 같이 하면 배수가 되도록 1을 한번에 빼서 while 문이 반복되는 횟수가 줄어든다.