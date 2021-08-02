# Silver 5_11723

# 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.
#
# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

import sys

m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    temp = sys.stdin.readline().strip().split()

    if len(temp) == 1:
        if temp[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()

    else:
        func, x = temp[0], temp[1]
        x = int(x)

        if func == "add":
            S.add(x)
        elif func == "remove":
            S.discard(x)
        elif func == "check":
            print(1 if x in S else 0)
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)



# === 메모리초과
from sys import stdin
input = stdin.readline

m = int(input())
s=[]

for i in range(m):
    a = input().split()
    if a[0] == 'add':
        s.append(a[1])
    elif a[0] == 'remove':
        if a[1] in s:
            del(s[s.index(a[1])])
        else:
            continue
    elif a[0] == 'check':
        if a[1] in s:
            print(1)
        else:
            print(0)
    elif a[0] == 'toggle':
        if a[1] in s:
            del (s[s.index(a[1])])
        else:
            s.append(a[1])
    elif a[0] == 'all':
        s = [x for x in range(1,21)]
    elif a[0] == 'empty':
        s=[]