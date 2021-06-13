# Bronze 3_2506
# 여러 개의 OX 문제로 만들어진 시험에서 연속적으로 답을 맞히는 경우에는 가산점을 주기 위해서
# 다음과 같이 점수 계산을 하기로 하였다.
# 1번 문제가 맞는 경우에는 1점으로 계산한다.
# 앞의 문제에 대해서는 답을 틀리다가 답이 맞는 처음 문제는 1점으로 계산한다.
# 또한, 연속으로 문제의 답이 맞는 경우에서 두 번째 문제는 2점, 세 번째 문제는 3점, ...,
# K번째 문제는 K점으로 계산한다. 틀린 문제는 0점으로 계산한다.

from sys import stdin

n = int(stdin.readline())
an = list(map(int,stdin.readline().split(' ')))
result = 0
sum = 0

for i in range(n):
    if an[i] == 1:
        sum += 1
        result += sum
    else:
        sum = 0

print(result)
