# 다익스트라 최단 경로 알고리즘
# 성능 O(V)번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색, V = 노드의 개수
# 전체 시간 복잡도 = O(V**2)

# 일반적으로 코딩 테스트의 최단 경로 문제에서 전체 노드의 개수가 5000개 이하면 이 코드로 해결 가능
# < 10000개가 넘어가는 문제라면?>>
# 우선순위 큐를 이용
# == 우선순위가 가장 높은 데이터를 가장 먼저 삭제

# 간선(이동거리? 비용?)이 동일하지 않음 == bfs, dfs 와 다름
# 매 상황에서 가장 비용이 적은 노드를 선택 == 그리디 알고리즘
# 음의 간선이 없을 때 정상 작동
# 동작 과정
# 1. 출발 노드 설정
# 2. 최단 거리 테이플 초기화
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택
# 4. 해당 노드를 거쳐 다른 노드로 가느는 비용을 계산, 테이블 갱신
# 5. 위 과정에서 3,4번을 반복

# 구현 팁
# 매 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해서 매 단계마다
# 1차원 테이블의 모든 원소를 확인(순차 탐색)한다.

import sys
Input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억 설정

# 노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())
# 시작 노드 번호를 입력
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 작성
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만듦
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print('INFINITY')
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])


