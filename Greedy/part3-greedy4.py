# Part3 그리디 문제 4: 만들 수 없는 금액
coin_cnt = int(input())
coin_list = list(map(int, input().split()))

coin_list.sort()
result = 1

# 정렬해서 앞 수부터 하나씩 더해가면 나올 수 있는 최소 수부터 구해진다.
# 그래서 1, 2, 3 이면 (if 1 < 1:), (if 3 < 2:), (if 6 < 3:)를 비교한다.
# 2, 4, 5가 생략 가능한 이유는??? 생략 가능해도 구할 수 있다고 판단할 수 있는 이유는???
# 이전 수에서 1이 없었으면 바로 1이 리턴됨
# 이전 수에 2가 없었으면 바로 2가 리턴됨
# 이전 수에 3이 없었으면 4가 리턴됨 (여기에서 이미 1과 2가 있다고 판단됨 => 즉 3이 존재함)
# 이전 수에 4가 없었다면 7이 리턴됨 (여기에서 이미 1과, 2와, 3과, 4와, 5가 있다고 판단됨)

for coin in coin_list:
		if result < coin: break
		result += coin

print(result)