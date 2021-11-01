# Silver 1_1074

# 한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다.
# 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.
# N > 1인 경우, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.
# N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.
# 0행 0열부터 시작

N, r, c = map(int, input().split())
cnt = 0

while N > 1:
    size = (2 ** N) // 2
    if r < size and c < size: # 2사분면
        pass
    elif r < size and c >= size: # 1사분면
        cnt += size ** 2
        c -= size
    elif r >= size and c < size: # 3사분면
        cnt += size ** 2 * 2
        r -= size
    elif r >= size and c >= size: # 4사분면
        cnt += size ** 2 * 3
        r -= size
        c -= size
    N -= 1

if r == 0 and c == 0:
    print(cnt)
if r == 0 and c == 1:
    print(cnt + 1)
if r == 1 and c == 0:
    print(cnt + 2)
if r == 1 and c == 1:
    print(cnt + 3)