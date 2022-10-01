# 로그파일 재정렬

# 로그를 재정렬하라.
# 기준 1. 로그의 가장 앞 부분은 식별자이다.
# 기준 2. 문자로 구성된 로그가 숫자 로그보다 앞에온다.
# 기준 3. 식별자는 순서에 영향을 끼치치 않지만, 문자가 동일할 경우 식별자 순으로 한다.
# 기준 4. 숫자 로그는 입력 순서대로 한다.

inputData = ["dig1 8 1 5 1", "let1 art can","dig2 3 6", "let2 own kit dig", "let3 art zero"]

def mySolution(logList):
		digits, letters = [], []
  
		for log in logList:
				# 숫자로만 이뤄졌는지 확인
				if log.split()[1].isdigit(): digits.append(log)
				else: letters.append(log)

		letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
		return letters + digits

print( mySolution(inputData) )