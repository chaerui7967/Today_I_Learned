# Bronze 3_2355
# 두 정수 A와 B가 주어졌을 때, 두 정수 사이에 있는 수의 합을 구하는 프로그램을 작성하시오.
# 사이에 있는 수들은 A와 B도 포함한다

A, B = map(int, input().split())

m = max(A, B)
n = min(A, B)

# print(sum(range(n, m+1)))

sum = (A + B) * (m - n + 1) / 2
print(int(sum))

# 시그마 덧셈공식
# 1~n까지 덧셈
# n(n+1)/2
