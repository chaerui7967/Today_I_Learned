# # Bronze 2_1159
# 누가 선발인지 기억하기 쉽게 하기 위해 성의 첫 글자가 같은 선수 5명을 선발하려고 한다.
# 만약, 성의 첫 글자가 같은 선수가 5명보다 적다면, 상근이는 내일 있을 친선 경기를 기권하려고 한다.
# 상근이는 내일 경기를 위해 뽑을 수 있는 성의 첫 글자를 모두 구해보려고 한다.

# 첫째 줄에 선수의 수 N (1 ≤ N ≤ 150)이 주어진다. 다음 N개 줄에는 각 선수의 성이 주어진다.

# 상근이가 선수 다섯 명을 선발할 수 없는 경우에는 "PREDAJA"를 출력한다. PREDAJA는 크로아티아어로 항복을 의미한다.
# 선발할 수 있는 경우에는 가능한 성의 첫 글자를 사전순으로 공백없이 모두 출력한다.

from sys import stdin
from collections import Counter

input = stdin.readline
n = int(input())
player = []
fn = []
cnt = 0
for i in range(n):
    a = input()
    player.append(a[0])
player_count = Counter(player)

for i,j in player_count.items():
    if j >= 5:
        fn.append(i)
        cnt += 1
fn.sort()

if cnt == 0:
    print('PREDAJA')
else:
    for i in fn:
        print(i, end='')

# 입력                 출력
# 6                   PREDAJA
# michael
# jordan
# lebron
# james
# kobe
# bryant