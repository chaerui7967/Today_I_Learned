# 최소 공통 조상
# 참고 문제 BOJ 11437번
# 문제 예시
# n개의 정점으로 이루어진 트리가 주어지고 트리의 각 정점은 1번부터 n번까지 번호가 매겨져 있으며
# 루트는 1번이다. 두 노드의 쌍 m개가 주어졌을 때, 두 노드의 가장 가까운 공통 조상이 몇 번인지 출력

# 기본 알고리즘
# 1. 모든 노드에 대해 깊이를 계산
# 2. 최소 공통 조상을 찾을 두 노드를 확인
#     1. 먼저 두 노드의 깊이가 동일하도록 거슬러 올라감
#     2. 이후에 부모가 같아질 때까지 반복적으로 두 노드의 부모 방향으로 거슬러 올라감
# 3. 모든 LCA 연산에 대해 2번 반복

# 시간 복잡도
# 매 쿼리마다 부모방향으로 거슬러 올라가기 위해 최악의 경우 O(N)의 시간복잡도가 요구
# 따라서 모든 쿼리를 처리할 때의 시간 복잡도는 O(NM)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5)) # 런타임 오류 피하기
n = int(input())

parent = [0] * (n+1)  # 부모 노드 정보
d = [0] * (n+1)  # 각 노드까지의 깊이
c = [0] * (n+1)  # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n+1)] # 그래프 정보

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 깊이를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]: # 이미 깊이를 구했다면 패스
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

dfs(1, 0)  # 루트 노드는 1번 노드

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a,b))
