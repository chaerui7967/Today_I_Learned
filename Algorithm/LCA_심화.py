# 최소 공통 조상 알고리즘 심화
# 예시 문제 = BOJ 11438
# n개의 정점으로 이루어진 트리가 주어짐
# 트리의 각 정점은 1번부터 n번까지 번호가 매겨져 있고, 루트는 1번
# 두 노드의 쌍 m개가 주어졌을 때, 두 노드의 가장 가까운 조상 출력

# 기존 코드 개선
# 2의 제곱형태로 거슬러 올라가도록 하면 O(logN)의 시간복잡도
# 메모리를 더 사용하여 각 노드에 대해 2**i번째 부모의 정보를 기록
# 다이나믹 프로그래밍을 통해 시간복잡도를 개선할 수 있다
# 세그먼트 트리를 이용하는 방법도 존재
# 매 쿼리마다 부모를 거슬러 올라가기 위해 O(logN)의 시간복잡도를 쓰므로
# 따라서 모든 쿼리를 처리할 때 시간 복잡도는 O(MlogN)이 된다.

import sys
input = sys.stdin.readline  # 시간 초과를 피하기 위해 빠른 입력 함수 사용
sys.setrecursionlimit(int(1e5))  # 런타임 오류 회피를 위한 재귀 깊이 제한
LOG = 21 # 2^20 = 1000000

n = int(input())
parent = [[0] * LOG for _ in range(n+1)]  # 부모 노드 정보
d = [0] * (n+1)  # 각 노드까지의 깊이
c = [False] * (n+1)  # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n+1)]  # 그래프 정보

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작해 깊이를 구하는 함수
def dfs(x,depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]:  # 이미 깊이를 구했다면 패스
            continue
        parent[y][0] = x
        dfs(y, depth + 1)

# 전체 부모 관계를 설정하는 함수
def set_parent():
    dfs(1,0)  # 루트 노드는 1번
    for i in range(1,LOG):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

# A와 B의 최소 공통 조상을 찾는 함수
def lca(a,b):
    # b가 더 깊도록 설정
    if d[a] > d[b]:
        a,b = b,a
    # 먼저 깊이가 동일하도록
    for i in range(LOG - 1, -1, -1):
        if d[b] - d[a] >= (1 << i):  # 2**i
            b = parent[b][i]
    # 부모가 같아지도록
    if a == b:
        return a
    for i in range(LOG-1,-1,-1):
        # 조상을 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    # 이후에 부모가 찾고자 하는 조상
    return parent[a][0]

set_parent()

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))