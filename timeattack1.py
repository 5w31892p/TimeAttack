# 각도기
def solution(angle):
    if angle < 90:
        result = 1
    elif angle == 90:
        result = 2
    elif 90 < angle < 180:
        result = 3
    else:
        result = 4
    return result


# 할인
def solution(price):
    discount5 = price * 0.05
    discount10 = price * 0.10
    discount20 = price * 0.20
    if price < 100000:
        result = price
    elif price >= 100000 and price < 300000:
        result = price - discount5
    elif price >= 300000 and price < 500000:
        result = price - discount10
    else:
        result = price - discount20

    return int(result)


# 369
def solution(order):
    answer = 0
    s_order = str(order)
    for num in s_order:
        if num == '3' or num == '6' or num == '9':
            answer += 1

    return answer
