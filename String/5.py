# 그룹 애너그램

# 문자열 배열을 받아 애너그램 단위로 그룹핑하라.
# 애너그램이란 일종의 언어유희로 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것을 말한다.

import collections


inputData = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

def mySolution(strList):
		sortedStr = sorted(strList)
		anagrams = collections.defaultdict(list)

		for word in sortedStr:
				# 단어 정렬
				sortedStr = ''.join(sorted(word))
				# 정렬 딕셔너리에 추가
				anagrams[sortedStr].append(word)
		
		return list(anagrams.values())


print(mySolution(inputData))