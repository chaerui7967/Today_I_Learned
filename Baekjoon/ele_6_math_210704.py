# Bronze 1_2702

# 두 정수 a와 b 최소공배수는 두 수의 공통된 배수 중 가장 작은 수이고,
# 최대공약수는 두 수의 공통된 약수중 가장 큰 수이다.
# a와 b가 주어졌을 때, 최소공배수와 최대공약수를 구하는 프로그램을 작성하시오.

import math as ma

def lcm(a,b): return a*b//ma.gcd(a,b)

t = int(input())

for _ in range(t):
    a, b = map(int,input().split())
    print(lcm(a,b),ma.gcd(a,b))
