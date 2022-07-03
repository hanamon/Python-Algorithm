# Part3 구현 문제 2: 문자열 재정렬

# 알파벳 대소문자 + 숫자가 입력으로 주어진다.
# 알파벳을 오름차순으로 정렬하고 모든 입력 숫자의 합을 이어서 출력한다.

from functools import reduce

sorted_str = sorted(input())

total_number = str(reduce(lambda acc, cur: acc + cur, [ int(str) for str in list(sorted_str) if str >= '0' and str <= '9' ]))
alphabets = ''.join([ str for str in list(sorted_str) if str > '9' ])

print(alphabets + total_number)