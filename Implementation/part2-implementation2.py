# 구현 문제 2 : 시각

# 모든 시간을 초로 변환한다.
# 초가 카운트 되면서 시, 분, 초를 업데이트한다.
# 문자열로 변환 후 '3'이 존재하는지 확인한다.

hour, minute, second = int(input()), 59, 59
total_secound = (hour * 60 * 60) + (minute * 60) + second
three_count = 0

while total_secound > 0:
    if second > 0: 
        second -= 1
    else:
        if minute > 0:
            minute -= 1
            second = 59
        else:
            if hour > 0:
                hour -= 1
                minute = 59
                second = 59

    str_time = str(hour) + ':' + str(minute) + ':' + str(second)
    if str_time.find('3') != -1: three_count += 1

    total_secound -= 1

print(three_count)