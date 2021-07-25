# Silver 4_1978

# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

from sys import stdin
input = stdin.readline

n = int(input())
sosu = list(map(int, input().split()))

def prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
count = 0
for i in sosu:
    if prime(i):
        count += 1
print(count)