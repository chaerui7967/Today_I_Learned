# 금광 문제
# n * m 크기의 금광이 있다. 금광은 1 * 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어 있다.
# 채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작한다.
# 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있다.
# 이후에 m-1번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 한다.
# 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하시오.

# 해결 아이디어
# 1. 왼쪽 위에서 오는 경우
# 2. 왼쪽 아래에서 오는 경우
# 3. 왼쪽에서 오는 경우

# array[i][j] = i행 j열에 존재하는 금의 양
# dp[i][j] = i행 j열까지의 최적 해
# dp[i][j] = array[i][j] + max(dp[i-1][j-1],dp[i][j-1],dp[i+1][j-1])

# 입력조건
# 테스트 케이스 T가 입력
# n,m 입력
# n*m 개의 위치에 매장된 금의 개수 입력


# 테스트 케이스 입력
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int,input().split())
    array = list(map(int,input().split()))
    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index : index + m])  # 2차원 테이블로 만들기 위해 m개씩 슬라이싱
        index += m
    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0: left_up = 0
            else: left_up = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1: left_down = 0
            else: left_down = dp[i+1][j-1]
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up,left_down,left)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)

# 예시                               출력
# 2                                 19
# 3 4                               16
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
