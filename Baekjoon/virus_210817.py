# Silver 3_2606

# 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다.
# 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
# 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때,
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

# dfs 사용 (깊이 우선 탐색)
n = int(input())
t = int(input())
s = [[0] * n for i in range(n)]
visit = [0 for i in range(n)]
for i in range(t):
    a, b = map(int, input().split())
    s[a-1][b-1] = 1
    s[b-1][a-1] = 1

def dfs(v):
    visit[v] = 1
    for i in range(n):
        if s[v][i] == 1 and visit[i] == 0:
            dfs(i)
dfs(0)
cnt = 0

for i in range(1,n):
    if visit[i] == 1:
        cnt += 1
print(cnt)

# ===== bfs 방식 (넓이 우선 탐색)

from sys import stdin
read = stdin.readline
dic={}
for i in range(int(read())):
    dic[i+1] = set()
for j in range(int(read())):
    a, b = map(int,read().split())
    dic[a].add(b)
    dic[b].add(a)

def bfs(start, dic):
    queue = [start]
    while queue:
        for i in dic[queue.pop()]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
visited = []
bfs(1, dic)
print(len(visited)-1)



# ===== dfs 방식 (깊이 우선탐색)

from sys import stdin
read = stdin.readline
dic={}
for i in range(int(read())):
    dic[i+1] = set()
for j in range(int(read())):
    a, b = map(int,read().split())
    dic[a].add(b)
    dic[b].add(a)

def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)
visited = []
dfs(1, dic)
print(len(visited)-1)