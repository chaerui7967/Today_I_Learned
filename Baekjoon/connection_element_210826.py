# Silver 2_11724

# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

import sys
sys.setrecursionlimit(10000)  # 재귀 호출시 기본값이 1000이지만 그 깊이를 지정해줌
input = sys.stdin.readline

n, m = map(int, input().split())
s = [[0] * (n + 1) for i in range(n + 1)]
visit = [0 for i in range(n + 1)]
cnt = 0

def dfs(i):
    visit[i] = 1
    for k in range(1, n + 1):
        if s[i][k] == 1 and visit[k] == 0:
            dfs(k)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    s[a][b] = 1
    s[b][a] = 1

for i in range(1, n + 1):
    if visit[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)
