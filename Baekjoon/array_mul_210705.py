# Bronze 1_2740

# N*M크기의 행렬 A와 M*K크기의 행렬 B가 주어졌을 때, 두 행렬을 곱하는 프로그램을 작성하시오.

# 파이썬 행렬 곱셈은 N*M 행렬과 M*K 행렬이 만나 N*K행렬을 만든 다는 것만 기억하면 된다.
N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
B = []
for _ in range(M):
    B.append(list(map(int, input().split())))


#행렬 곱셈
C = [[0 for _ in range(K)] for _ in range(N)]

for n in range(N):
    for k in range(K):
        for m in range(M):
            C[n][k] += A[n][m] * B[m][k]

#출력문
for i in C:
    for j in i:
        print(j, end = ' ')
    print()


# -------------
# 런타임 에러
import numpy as np

n1, m1 = map(int,input().split())
arr1 = []
for i in range(n1):
    arr1.append(list(map(int, input().split())))
arr1 = np.array(arr1)

n2, m2 = map(int, input().split())
arr2 = []
for i in range(n2):
    arr2.append(list(map(int, input().split())))
arr2 = np.array(arr2)

arr3 = np.dot(arr1, arr2)

for i in range(arr3.__len__()):
    print(arr3[i])
