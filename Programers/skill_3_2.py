# Q2 카카오 기출
# https://programmers.co.kr/learn/courses/30/lessons/60063
# 로봇개발자 "무지"는 한 달 앞으로 다가온 "카카오배 로봇경진대회"에
# 출품할 로봇을 준비하고 있습니다.
# 준비 중인 로봇은 2 x 1 크기의 로봇으로 "무지"는 "0"과 "1"로 이루어진
# N x N 크기의 지도에서 2 x 1 크기인 로봇을 움직여 (N, N) 위치까지
# 이동 할 수 있도록 프로그래밍을 하려고 합니다.
# 로봇이 이동하는 지도는 가장 왼쪽, 상단의 좌표를 (1, 1)로 하며 지도 내에 표시된
# 숫자 "0"은 빈칸을 "1"은 벽을 나타냅니다.
# 로봇은 벽이 있는 칸 또는 지도 밖으로는 이동할 수 없습니다.
# 로봇은 처음에 아래 그림과 같이 좌표 (1, 1) 위치에서 가로방향으로 놓여있는 상태로 시작하며,
# 앞뒤 구분없이 움직일 수 있습니다.

# 로봇이 움직일 때는 현재 놓여있는 상태를 유지하면서 이동합니다.
# 예를 들어, 위 그림에서 오른쪽으로 한 칸 이동한다면 (1, 2), (1, 3) 두 칸을 차지하게 되며,
# 아래로 이동한다면 (2, 1), (2, 2) 두 칸을 차지하게 됩니다.
# 로봇이 차지하는 두 칸 중 어느 한 칸이라도 (N, N) 위치에 도착하면 됩니다.

# 로봇은 다음과 같이 조건에 따라 회전이 가능합니다.

# 위 그림과 같이 로봇은 90도씩 회전할 수 있습니다.
# 단, 로봇이 차지하는 두 칸 중, 어느 칸이든 축이 될 수 있지만,
# 회전하는 방향(축이 되는 칸으로부터 대각선 방향에 있는 칸)에는 벽이 없어야 합니다.
# 로봇이 한 칸 이동하거나 90도 회전하는 데는 걸리는 시간은 정확히 1초 입니다.

# "0"과 "1"로 이루어진 지도인 board가 주어질 때,
# 로봇이 (N, N) 위치까지 이동하는데 필요한 최소 시간을 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# board의 한 변의 길이는 5 이상 100 이하입니다.
# board의 원소는 0 또는 1입니다.
# 로봇이 처음에 놓여 있는 칸 (1, 1), (1, 2)는 항상 0으로 주어집니다.
# 로봇이 항상 목적지에 도착할 수 있는 경우만 입력으로 주어집니다.

from collections import deque


def solution(board):
    def my_append(t, d):
        # 방문한적이 없을 때 추가해줌
        if t not in visited:
            q.append((t, d))
            visited.add(t)

    n = len(board)

    q = deque()
    visited = set()  # set으로 만들어야 시간복잡도 줄인다
    q.append(((0, 0, 0, 1), 0))
    visited.add((0, 0, 0, 1))
    while q:
        t, d = q.popleft()  # t: 해당 좌표, d: 거리
        x1, y1, x2, y2 = t

        # 가로 도착
        if x1 == n - 1 and x2 == n - 1 and y1 == n - 2 and y2 == n - 1:
            return d
        # 세로 도착
        if x1 == n - 2 and x2 == n - 1 and y1 == n - 1 and y2 == n - 1:
            return d

        d += 1  # 끝에 도착하지 않았으므로 거리를 1 늘림

        # 움직이는 모든 조건
        # 가로 일 때
        if x1 == x2:
            # 오른쪽 이동
            if y2 + 1 < n and board[x2][y2 + 1] == 0:
                t = (x1, y1 + 1, x2, y2 + 1)
                my_append(t, d)
            # 왼쪽 이동
            if y1 - 1 >= 0 and board[x1][y1 - 1] == 0:
                t = (x1, y1 - 1, x2, y2 - 1)
                my_append(t, d)

            # 위로 이동 | 가능하면 오른쪽 위 회전도 가능, 횐쪽 위 회전도 가능
            if x1 - 1 >= 0 and board[x1 - 1][y1] == 0 and board[x2 - 1][y2] == 0:
                t = (x1 - 1, y1, x2 - 1, y2)
                my_append(t, d)
                # 오른쪽 위 회전
                t = (x1 - 1, y1 + 1, x2, y2)
                my_append(t, d)
                # 왼쪽 위 회전
                t = (x2 - 1, y2 - 1, x1, y1)
                my_append(t, d)
            # 아래로 이동 | 가능하면 오른쪽 아래 회전도 가능, 왼쪽 아래 회전도 가능
            if x1 + 1 < n and board[x1 + 1][y1] == 0 and board[x2 + 1][y2] == 0:
                t = (x1 + 1, y1, x2 + 1, y2)
                my_append(t, d)
                # 오른쪽 아래 회전
                t = (x2, y2, x1 + 1, y1 + 1)
                my_append(t, d)
                # 왼쪽 아래 회전
                t = (x1, y1, x2 + 1, y2 - 1)
                my_append(t, d)

        # 세로 일 때
        elif y1 == y2:
            # 오른쪽 이동
            if y1 + 1 < n and board[x1][y1 + 1] == 0 and board[x2][y2 + 1] == 0:
                t = (x1, y1 + 1, x2, y2 + 1)
                my_append(t, d)
                # 오른쪽 아래 회전
                t = (x2, y2, x1 + 1, y1 + 1)
                my_append(t, d)
                # 오른쪽 위 회전
                t = (x1, y1, x2 - 1, y2 + 1)
                my_append(t, d)
            # 왼쪽 이동
            if y1 - 1 >= 0 and board[x1][y1 - 1] == 0 and board[x2][y2 - 1] == 0:
                t = (x1, y1 - 1, x2, y2 - 1)
                my_append(t, d)
                # 왼쪽 아래 회전
                t = (x1 + 1, y1 - 1, x2, y2)
                my_append(t, d)
                # 왼쪽 위 회전
                t = (x2 - 1, y2 - 1, x1, y1)
                my_append(t, d)
            # 위로 이동
            if x1 - 1 >= 0 and board[x1 - 1][y1] == 0:
                t = (x1 - 1, y1, x2 - 1, y2)
                my_append(t, d)
            # 아래로 이동
            if x2 + 1 < n and board[x2 + 1][y1] == 0:
                t = (x1 + 1, y1, x2 + 1, y2)
                my_append(t, d)