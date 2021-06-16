# 위상 정렬
# 방향성을 거스르지 않도록 전체 노드를 나열
# 예시 - 선수과목을 고려한 학습 순서 설정
# 진입차수(indegree) : 특정한 노드로 들어오는 간선의 개수
# 진출차수(outdegree) : 특정한 노드에서 나가나는 간선의 개수
# 큐를 이용
# 1. 진입차수가 0인 모든 노드를 큐에 넣는다
# 2. 큐가 빌 때까지 다음 과정 반복
#     1. 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거
#     2. 새롭게 진입차수가 0이 된 노드를 큐에 넣음
# ==> 결과적으로 각 노드가 큐에 들어온 순서가 위상 정렬을 수행한 결과와 같다.
# 사이클이 없는 방향 그래프(DAG_Direct Acyclic Graph)여야 가능
# 위상 정렬에서는 여러가지 답이 존재 가능 -- 한 단계에서 큐에 새롭게 들어가는 원소가 2개이상인 경우
# 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재
# -- 사이클이 포함된 원소 중에서 어떠한 원소도 큐에 들어가지 못함
# 스택을 활용한 DFS를 이용해 위상정렬 가능
# 위상정렬을 위해 차례대로 모든 노드를 확인하며 각 노드에서 나가는 간선을 차례대로 제거
# 위상정렬의 시간 복잡도 O(V+E)

from collections import deque

# 노드의 개수와 간선의 개수를 입력
v, e = map(int,input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # 정점 A에서 B로 이동 가능
    # 진입 차수를 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = []  # 알고리즘 수행 결과를 담을 리스트
    q = deque()  # 큐 기능을 위한 deque 라이브러리 사용
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌 때까지 반본
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()

# 입력 예시        ====> 1 2 5 3 6 4 7
# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4
