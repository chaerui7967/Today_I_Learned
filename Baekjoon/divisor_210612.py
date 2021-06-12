# Bronze 3_2501
# 두 개의 자연수 N과 K가 주어졌을 때,
# N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.

n, k = map(int,input().split())

ic = list()

for i in range(1, n+1):
    if n % i == 0:
        ic.append(i)

if len(ic) >= k:
    print(ic[k-1])
else:
    print(0)

# 다른 방법 알고리즘 사용

def get_divisor(n):
    n = int(n)
    divisors = []
    divisors_back = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisors.append(i)
            if (i != (n // i)):
                divisors_back.append(n//i)

    return divisors + divisors_back[::-1]

print(get_divisor(n)[k-1])