# Bronze 1_1453

# 세준이의 피시방에는 1번부터 100번까지 컴퓨터가 있다.
# 들어오는 손님은 모두 자기가 앉고 싶은 자리에만 앉고싶어한다. 따라서 들어오면서 번호를 말한다.
# 만약에 그 자리에 사람이 없으면 그 손님은 그 자리에 앉아서 컴퓨터를 할 수 있고, 사람이 있다면 거절당한다.
# 거절당하는 사람의 수를 출력하는 프로그램을 작성하시오. 자리는 맨 처음에 모두 비어있고,
# 어떤 사람이 자리에 앉으면 자리를 비우는 일은 없다.

from sys import stdin
input = stdin.readline
N = int(input())
PC_Georgia = list(map(int, input().split()))
PC_checkmate = [0] * 101 #PC방 자리
PC_refused = 0 #거절당한 사람

for i in PC_Georgia:
    if PC_checkmate[i] != 0:
        PC_refused += 1
    else:
        PC_checkmate[i] += 1

print(PC_refused)