# Bronze 3_2476
# 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.

# 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다.
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다.
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.

# N(2 ≤ N ≤ 1,000)명이 주사위 게임에 참여하였을 때,
# 가장 많은 상금을 받은 사람의 상금을 출력하는 프로그램을 작성하시오.

# 리스트를 사용

from sys import stdin
n = int(stdin.readline())

hap = []

for i in range(n):
    a = list(map(int, stdin.readline().split(' ')))
    if a.count(max(a)) == 3:
        hap.append(max(a)*1000+10000)
        continue
    elif a.count(max(a)) == 2:
        hap.append(max(a)*100 + 1000)
        continue
    elif a.count(min(a)) == 2:
        hap.append(min(a)*100 + 1000)
        continue
    else:
        hap.append(max(a)*100)

print(max(hap))

# 리스트를 사용하지 않는 방법

n = int(input())

max_reward = 0
for _ in range(n):
    reward = 0
    d1, d2, d3 = map(int, input().split())
    if d1 == d2 == d3:
        reward = 10000 + d1 * 1000
    elif d1 == d2:
        reward = 1000 + d1 * 100
    elif d2 == d3:
        reward = 1000 + d2 * 100
    elif d1 == d3:
        reward = 1000 + d1 * 100
    elif d1 != d2 != d3:
        reward = max(d1, d2, d3) * 100
    if max_reward < reward:
        max_reward = reward

print(max_reward)