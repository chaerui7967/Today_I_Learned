# 벨만 포드 알고리즘
# 예시 문제 - boj '타임머신' 11657번
# 다익스트라 알고리즘에서 음수 간선이 포함된다면? == 가능
# 음수 간선의 순환이 포함되면?
# 음의 무한인 노드가 생성됨 ==> 벨만 포드 최단 경로 알고리즘
# 시간 복잡도 O(VE)

# 다익스트라 알고리즘
# 1. 매번 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
# 2. 음수 간선이 없다면 최적의 해를 찾을 수 있다

# 벨만 포드 알고리즘
# 1. 매번 모든 간선을 전부 확인
#     -  따라서 다익스트라 알고리즘에서의 최적의 해를 항상 포함
# 2. 다익스트라 알고리즘에 비해 시간이 오래 걸리지만 음수 간선 순환을 탐지

import sys
input = sys.stdin.readline()
INF = int(1e9)

def bf(start):
    # 시작 노드에 대해서 초기화
    dist[start] = 0
    # 전체 n번의 라운드를 반복
    for i in range(n):
        # 매 반복마다 '모든 간선'을 확인
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == n-1:
                    return True
    return False

# 노드의 개수, 간선의 개수를 입력
n, m = map(int,sys.stdin.readline().split())
# 모든 간선에 대한 정보를 담는 리스트 생성
edges = []
# 최단 거리 테이블을 모두 무한으로 초기화
dist = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    edges.append((a,b,c))

# 벨만 포드 알고리즘 수행
negative_cycle = bf(1) # 1번 노드가 시작 노드

if negative_cycle:
    print('-1')
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, n+1):
        # 도달할 수 없는 경우, -1 출력
        if dist[i] == INF:
            print('-1')
        # 도달할 수 있는 경우 거리 출력
        else:
            print(dist[i])
