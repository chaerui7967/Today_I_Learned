# 2진수 8진수
# 2진수가 주어졌을 때, 8진수로 변환하는 프로그램을 작성하시오.

from sys import stdin

input = stdin.readline
bi = input()
ten = int(bi, 2)
print(oct(ten)[2:])