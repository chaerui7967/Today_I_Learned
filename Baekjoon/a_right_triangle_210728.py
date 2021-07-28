# Bronze 3_4153

# 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

from sys import stdin
input = stdin.readline

a, b, c = map(int, input().split())

while a != 0 and b != 0 and c != 0:
    if a**2 + b**2 == c**2:
        print('right')
    elif a**2 + c**2 == b**2:
        print('right')
    elif b**2 + c**2 == a**2:
        print('right')
    else:
        print('wrong')
    a, b, c = map(int, input().split())