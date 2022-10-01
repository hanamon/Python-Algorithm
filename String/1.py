# 주어진 문자열이 팰린드롬인지 확인, 대소문자 구분 없음, 영문자와 숫자만 대상으로 함
# input: "A man, a plan, a canal: Panama"
# output: true

# input: "race a car"
# output: false

# 팰린드롬이란?
# 앞뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어 또는 문장.
# 우리말로는 '회문'이라고 함.

import re

inputData = 'A man, a plan, a canal: Panama'

def getStringAndNumber(string):
  return re.sub(r'[^0-9A-Za-z]', '', string)

def mySolution(string):
  lowerString = getStringAndNumber(string).lower()
  if lowerString != lowerString[::-1]: return False
  return True
  
print(mySolution(inputData))