# Silver 5_10989

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오

from sys import stdin
input = stdin.readline

n = int(input())
c_list = [0] * 10001
for i in range(n):
    num = int(input())
    c_list[num] = c_list[num] + 1
for i in range(10001):
    if c_list[i] != 0:
        for j in range(c_list[i]):
            print(i)

# =======시간, 메모리 초과=======
n = int(input())
dict = {}
for i in range(n):
    num = int(input())

    if num not in dict.keys():
        dict[num] = 1
    else:
        dict[num] = dict[num] + 1
sorted_dict = sorted(dict.items())

for i in range(len(sorted_dict)):
    for j in range(sorted_dict[i][1]):
        print(sorted_dict[i][0])