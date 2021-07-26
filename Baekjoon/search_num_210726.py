# Silver 4_1920

# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 집합 자료형 사용
from sys import stdin, stdout
input = stdin.readline

n = int(input())
a = set(input().split())
m = int(input())
b = input().split()

for l in b:
    stdout.write('1\n') if l in a else stdout.write('0\n')


# === 이분 탐색 알고리즘 --성공
from sys import stdin
input = stdin.readline

n = int(input())
a = sorted(map(int, input().split()))
m = int(input())
b = map(int, input().split())

def binary(l, a, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == a[m]:
        return 1
    elif l < a[m]:
        return binary(l,a,start, m-1)
    else:
        return binary(l,a, m+1, end)

for l in b:
    start = 0
    end = len(a)-1
    print(binary(l, a, start, end))


# ====== 시간초과
from sys import stdin
input = stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
s = list(map(int, input().split()))

for i in s:
    if i in a:
        print(1)
    else:
        print(0)