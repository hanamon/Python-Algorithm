# 가장 긴 팰린드롬 부분 문자열을 출력하라.

# 컴퓨터 과학의 오랜 문제 중에 '최장 공통 부분 문자열(Longest Common Substring)이라는 문제가 있다.
# 여러 개의 입력 문자열이 있을 때 서로 공통된 가장 긴 부분 문자열을 찾는 문제로 다이나믹 프로그래밍으로 풀 수 있는 전형적인 문제다.
# 여기서는 좀 더 직관적이고 성능이 좋은 투 포인터가 중앙을 중심으로 확장하는 형태로 풀이되어있다.

def longestPalindrmon(str):
		# 팰린드롬 판별 및 추 포인트 확장
		def expand(left, right):
			while (
     		left >= 0  
   			and right < len(str)  
        and str[left] == str[right]
      ):
				left -= 1
				right += 1
			return str[left + 1:right]
    
    # 해당 사항이 없을 때 빠르게 리턴
		if len(str) < 2 or str == str[::-1]: return str

		result = ''
		# 슬라이딩 윈도우 우측으로 이동
		for i in range(len(str) - 1):
				result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
    
		return result

print(longestPalindrmon('babad'))