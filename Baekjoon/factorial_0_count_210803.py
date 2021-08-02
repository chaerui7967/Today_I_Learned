# Silver 4_1676

# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

# def fac(n):
#     if n > 1:
#         return n*fac(n-1)
#     else:
#         return 1

from functools import reduce

def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n+1))

# ======== 펙토리알 구현
# 5일때 120으로 0이 1개
# 10일 때 3628800으로 0이 2개

n = int(input())
str(factorial_reduce(n)).count(0)  ## 맨뒤 0을 구하는 거기때문에 틀림

# === 정답 n의 범위가 500이하이므로
N = int(input())
print(N//5 + N//25 + N//125)

# 곱했을 때 뒷자리가 0이 나오는 경우는 2, 5, 10, 5의 개수가 0의 개수
# === 런타임 에러
from sys import stdin
input = stdin.readline()

n = int(input())
count = 0

while n > 5:
    count += n//5

    n //= 5
print(count)

