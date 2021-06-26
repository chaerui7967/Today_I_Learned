# Gold 3_11437
# N(2 ≤ N ≤ 50,000)개의 정점으로 이루어진 트리가 주어진다.
# 트리의 각 정점은 1번부터 N번까지 번호가 매겨져 있으며, 루트는 1번이다.
# 두 노드의 쌍 M(1 ≤ M ≤ 10,000)개가 주어졌을 때,
# 두 노드의 가장 가까운 공통 조상이 몇 번인지 출력한다.

# 시간초과..
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))  # 런타임 오류 피하기
n = int(input())

parent = [0] * (n+1)  # 부모 노드 정보
d = [0] * (n+1)  # 각 노드까지의 깊이
c = [0] * (n+1)  # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n+1)]  # 그래프 정보 2중 리스트 [[---], [---]]

for _ in range(n-1):  # 그래프 정보 해당 번호와 연결된 번호
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 깊이를 구하는 함수
def dfs(x, depth):  # 깊이 우선 탐색을 통해서 부모 트리 입력
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]:  # 이미 깊이를 구했다면 패스
            continue
        parent[y] = x
        dfs(y, depth + 1)

# A와 B의 최소 공통 조상 검색
def lca(a, b):
    # 먼저 깊이가 동일하도록 맞춰줌
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    # 노드가 같아지도록
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

dfs(1, 0)  # 루트노트 설정, 루트 노드는 1번 노드

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a,b))


# 다른 방법 ----------------------------------------------------------------------------------------------
## 부모 저장을 2**2만큼 저장

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(cur, d):
    depth[cur] = d
    visited[cur] = True

    for child in tree[cur]:
        if not visited[child]:
            parent[child][0] = cur
            dfs(child, d+1)

def find_parent():
    for i in range(1, 21):
        for j in range(1, V+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a
    for i in range(20, -1, -1):
        if depth[b] - depth[a] >= (1<<i):
            b = parent[b][i]

    if a == b:
        return b

    for i in range(20, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]

def traversal(node):
    global answer

    answer += 1
    for i in tree[node]:
        traversal(i)



V = int(input())
tree = [[] for _ in range(V+1)]
for _ in range(V-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

depth = [0] * (V+1)
parent = [[0 for _ in range(21)] for _ in range(V+1)]
visited = [False] * (V+1)



dfs(1, 0)
find_parent()
M = int(input())
for _ in range(M):
    A, B = map(int, input().split())
    common_parent = lca(A, B)
    print(common_parent)


# 입력             출력
# 15              2
# 1 2             4
# 1 3             2
# 2 4             1
# 3 7             3
# 6 2             1
# 3 8
# 4 9
# 2 5
# 5 11
# 7 13
# 10 4
# 11 15
# 12 5
# 14 7   // 노드 정보
# 6   // 출력할 결과 갯수
# 6 11
# 10 9
# 2 6
# 7 6
# 8 13
# 8 15
