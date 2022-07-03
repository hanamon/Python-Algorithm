# Part3 구현 문제 1: 럭키 스트레이트

# '럭키 스트레이트' 기술은 점수가 특정 조건을 만족할 때만 사용가능
# 특정 조건이란 점수를 N이라고 했을 때
# 자릿수를 기준으로 점수 N을 반으로 나누어
# 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을 의미한다.

from functools import reduce

def get_total_score(acc, cur): return acc + cur

input_str = input().replace(',', '')
left_list = [ int(num) for idx, num in enumerate(list(input_str)) if idx < int(len(input_str) / 2) ]
right_list = [ int(num) for idx, num in enumerate(list(input_str)) if idx >= int(len(input_str) / 2) ]

left_total = reduce(get_total_score, left_list)
right_total = reduce(get_total_score, right_list)

if left_total == right_total: print('LUCKY')
else: print('READY')