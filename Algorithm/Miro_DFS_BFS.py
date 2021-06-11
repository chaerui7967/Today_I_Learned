# 미로탈출
# N X M 크기의 직사각형 형태의 미로
# 현재 위치는 (1,1) 미로의 출구는 (N, M)의 위치에 존재하며 한번에 한 칸씩 이동할 수 있다.
# 이때 괴물이 있는 부분을 0, 괴물이 없는 부분을 1로 표시
# 움직여야 하는 최소 칸의 개수를 구하시오.
# 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산

# 입력조건
# 첫째 줄에는 두 정수 N, M이 주어짐
# 다음 N개의 줄에는 각각 M개의 정수(0, 1)로 미로의 정보가 주어진다
# 각각의 수들은 공백 없이 붙여서 입력으로 제시된다
# 시작칸과 마지막 칸은 항상 1이다.

# 입력 예시   ====> 10
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

# BFS 구현
from collections import deque

def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브 러리 사용
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때가지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n -1][m - 1]

# N, M을 입력
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보를 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네가지 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 수행
print(bfs(0,0))