# Bronze 2_1551

# 크기가 N인 수열 A가 주어졌을 때, 세준이는 인접한 두 원소의 차이를 이용해서 크기가 N-1인 수열 B를 만들 수 있다.
# 예를 들어, A = {5,6,3,9,-1} 이었을 때, B = {6-5, 3-6, 9-3, -1-9} = {1,-3,6,-10}이 된다.
# 다른 말로 B[i] = A[i+1]-A[i]가 된다.
# 수열 A가 주어졌을 때, 세준이가 위의 방법을 K번 했을 때 나오는 수열을 구하는 프로그램을 작성하시오.

N, K = map(int, input().split())
li = list(map(int, input().split(',')))
for _ in range(K):
    t = [li[i+1]-li[i] for i in range(len(li)-1)]
    li = t
print(*li, sep=',')



# 출력 초과
n, k = map(int,input().split())
a = list(map(int,input().split(',')))
s = []
for i in range(k):
    for i in range(1, len(a)):
        s.append(a[i] - a[i-1])
for i in s[:-1]:
    print(i, end=',')
print(s[-1])