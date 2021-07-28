# Silver 4_10816

# 숫자 카드는 정수 하나가 적혀져 있는 카드이다.
# 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때,
# 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.


# ==== 이분탐색 활용
from sys import stdin
input = stdin.readline
_ = input()
N = sorted(map(int, input().split()))
_ = input()
M = map(int, input().split())

def binary(n, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2

    if n == N[m]:
        return N[start:end+1].count(n)
    elif n < N[m]:
        return binary(n,N,start,m-1)
    else:
        return binary(n, N, m+1, end)

n_dic = {}
for n in N:
    start = 0
    end = len(N)-1
    if n not in n_dic:
        n_dic[n] = binary(n, N, start, end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in M))

# ======== 시간초과
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
result = []
for i in arr2:
    if i in arr:
        result.append(arr.count(i))
    else:
        result.append(0)

print(result)