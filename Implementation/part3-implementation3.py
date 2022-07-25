# Part3 구현 문제 3: 문자열 압축

# 문자열 길이의 과반수 이상을 자르는 경우 의미 없음
# 문자열 길이의 반까지만 계산한다.

input_str = input() # aabbaccc
min_len = len(input_str)

for unit in range(1, int(len(input_str)/2)+1):
		# 문자열을 'unit'으로 압축한 값을 'min_len'과 비교한다.
		unit_list = []

		for str_idx in range(0, len(input_str), unit):
				add_str = input_str[str_idx:str_idx + unit]
    		# 10단위 100단위도 있기 때문에 문자열을 자르는 것을 '+' 문자 기준으로 하자
				unit_list.append('1+' + add_str)

				if str_idx > 0:
						last_el = unit_list[len(unit_list)-2]
						plus_idx = last_el.index('+')
      
						if last_el[plus_idx+1:] == add_str:
								unit_list[len(unit_list)-2] = str(int(last_el[0:plus_idx]) + 1) + '+' + add_str
								unit_list.pop()
     
		compressed_str = ''.join(list(map(lambda str: str[str.index('+')+1:] if (str[0] == '1') else (str[0:str.index('+')] + str[str.index('+')+1:]), unit_list)))
		min_len = min(min_len, len(compressed_str))

print(min_len)

# TODO: 정확성 70.0 나옴…