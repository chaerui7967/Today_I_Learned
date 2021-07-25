# Silver 5_11650

# 2차원 평면 위의 점 N개가 주어진다.
# 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

from sys import stdin
input = stdin.readline

n = int(input())
coord = []

for i in range(n):
    x, y = map(int, input().split())
    coord.append((x, y))

coord = list(set(coord))

coord.sort(key = lambda word: (word[0], word[1]))

for i in range(n):
    print(coord[i][0],coord[i][1])