# 그리디 문제 1 : 거스름돈

n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세
    n %= coin

print(count)

#-----------------------------------------------------------#


def greedy1 (n):
    count = 0
    coin_types = [500, 100, 50, 10]

    for coin in coin_types:
        count += (n // coin) # 1260 // 500 => 2를 count에 할당
        n %= coin # 1260 % 500 => 260을 n에 할

    return count

print(greedy1(1260))