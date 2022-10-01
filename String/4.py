# 가장 흔한 단어

# 금지된 단어를 제외한 가장 흔한게 등장하는 단어를 출력하라.
# 대소문자 구분 없음, 구두점(, .) 무시

import collections
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

def mySolution(paragraph, banned): 
		firstPreprocessed = re.sub(r'[^\w]', ' ', paragraph).lower().split()
		words = [word for word in firstPreprocessed]
		counts = collections.Counter(words)
		print(counts)
		return counts.most_common(1)[0][0]

print(mySolution(paragraph, banned))