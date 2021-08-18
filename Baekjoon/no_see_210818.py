# Silver 4_1764

# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때,
# 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

import sys

N, M = map(int, sys.stdin.readline().split())
N_list = [sys.stdin.readline().strip() for i in range(N)]
M_list = [sys.stdin.readline().strip() for i in range(M)]

# 교차하는 이름들을 찾는다
duplicate = list(set(N_list) & set(M_list))

print(len(duplicate))
for name in sorted(duplicate):
    print(name)

# ========시간초과
n, m = map(int, input().split())
hear = []
see = []

for _ in range(n):
    hear.append(input())
for _ in range(m):
    see.append(input())

cnt = 0
if len(hear) > len(see):
    for i in hear:
        if i in see:
            cnt += 1
            print(i)
else:
    for j in see:
        if j in hear:
            cnt += 1
            print(j)