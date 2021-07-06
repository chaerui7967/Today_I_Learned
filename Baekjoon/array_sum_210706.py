# Bronze 1_2738

# 첫째 줄에 행렬의 크기 N 과 M이 주어진다.
# 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다.
# 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다.
# N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
a = [list(map(int,input().split())) for _ in range(n)]  # 이중 리스트로 행렬을 받음

for i in range(n):  # 행n 만큼 반복
    b = list(map(int, input().split()))  # 해당 행에 대해 덧셈할 행을 입력
    for j in range(m):  # 열 m을 하나씩 가져오면서 덧셈할 행과 덧셈 수행
        print(a[i][j] + b[j], end=' ')  # 덤셈한 결과값 출력
    print()