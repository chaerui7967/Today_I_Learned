# Bronze 1_11050

# 자연수 과 정수 가 주어졌을 때 이항 계수 (n k)를 구하는 프로그램을 작성하시오.

# ==== 조합 사용(표준라이브러리)
from itertools import combinations

n, k = map(int, input().split())
arr = list(i for i in range(n))

print(len(list(combinations(arr, k))))


# === 팩토리얼 사용
from math import factorial

n, k = map(int, input().split())

b = factorial(n) // (factorial(k) * factorial(n - k))
print(b)