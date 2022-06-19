# Part3 그리디 문제 3: 문자열 뒤집기

# 1. 문자열을 입력받아 배열로 변환한다.
# 2. 0의 연속 구간과 1의 연속 구간을 각각 구한다.
# 3. 더 적은 수의 값을 리턴한다.

str = list(input())
result = 0
count_0 = 0
count_1 = 0

for idx, val in enumerate(str): # enumerate 내장 함수: 인덱스와 원소로 이루어진 터플(tuple)을 만들어 줌
		if str[idx] == '0': 
				if idx == 0: 
						count_0 += 1
						continue
				if str[idx] == str[idx-1]: continue
				count_0 += 1
    
		if str[idx] == '1':
				if idx == 0: 
						count_1 += 1
						continue
				if str[idx] == str[idx-1]: continue
				count_1 += 1

if count_0 < count_1:
		result = count_0
else: 
		result = count_1

# print(str)
# print(count_0)
# print(count_1)
print(result)