# Part3 그리디 문제 6: 무지의 먹방 라이브

# food_times: 각음식을 모두 먹는 데 필요한 시간이 음식의 번호 순서대로 들어있는 배열
# k: 방송이 중단된 시간
# 만약 더 섭취해야 할 음식이 없다면 -1을 리턴

#-------------------------------------------------#

# [방법 1] -- 효율성 X
# food_times = [1, 0, 0]
# food_times_len = len(food_times) - 1
# k = 5
# curr = 0

# for count in range(k-1):
#     if curr < food_times_len: 
#         if food_times[curr] != 0: food_times[curr] = food_times[curr]-1
#         curr += 1
#     else: curr = 0

# if curr == food_times_len: curr = 0
# else: curr + 1

# print(curr)

#-------------------------------------------------#

# [방법 2] -- 효율성 O
# K 만큼 돌지 않고 배열 크기 만큼만 돌게 할 수 없을까?

# 입력값
food_times = [0, 1355135, 0, 1000000000, 0, 24132412351, 135135, 13589, 1, 343, 13510]
k = 135135

# 솔루션 
def my_solution(food_times, k):
    food_times_len = len(food_times)
    turns = (k // food_times_len)
    minutes = k + 1
    currIdx = 0

    if sum(food_times) <= k: return -1

    while minutes > 0:
        # minutes에 따라 turns를 초기화한다.
        if currIdx == 0:
            turns = ((minutes - 1) // food_times_len)
            if turns <= 0: turns = 1

        # 배열을 초과하면 0으로 초기화한다.
        if currIdx > (food_times_len - 1):
            currIdx = 0
            continue

        # 음식이 없으면 다음으로 넘긴다.
        if food_times[currIdx] <= 0:
            currIdx += 1
            continue

        if food_times[currIdx] >= turns: 
            minutes -= turns
            food_times[currIdx] -= turns
        else:
            minutes -= food_times[currIdx]
            food_times[currIdx] = 0

        if minutes > 0: currIdx += 1

    return currIdx + 1

print('resulte:', my_solution(food_times, k))