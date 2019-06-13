# 문제5. 함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.

def sum(*number):
    result =0
    for tempNum in number:
        result+=tempNum
    return result

result = sum(1, 2, 3)
print(result)