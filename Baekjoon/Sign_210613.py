# Bronze 3_1247
# N개의 정수가 주어지면, 이 정수들의 합 S의 부호를 구하는 프로그램을 작성하시오.

# 내 입력
from sys import stdin
# stdin.readline()을 통해 입력을 빨게 받아옴
# 위의 메소드 없이 입력을 받아올 시 시간이 지체됨
S = [0,0,0]

for i in range(3):
    n = int(stdin.readline())
    for _ in range(n):
        s = int(stdin.readline())
        S[i] += s
    if S[i] == 0:
        S[i] = 0
    elif S[i] > 0:
        S[i] = '+'
    else:
        S[i] = '-'
    print(S[i])

# 다른방법
from sys import stdin

for _ in range(3):
    N = int(stdin.readline())
    li = [int(stdin.readline()) for i in range(N)]
    if sum(li) == 0:
        print("0")
    elif sum(li) > 0:
        print("+")
    else:
        print("-")