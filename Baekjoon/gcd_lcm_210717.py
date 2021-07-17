# Silver 5_2609

# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

from math import gcd, lcm

n, m = map(int,input().split())

print(gcd(n,m))
print(lcm(n,m))