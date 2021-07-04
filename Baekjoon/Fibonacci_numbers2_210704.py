# Bronze 1_2748

# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다.
# 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
# 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
# n=17일때 까지 피보나치 수를 써보면 다음과 같다.
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
#
# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

# dp사용 -- 매핑

import sys

N = int(sys.stdin.readline())
arr = [0 for _ in range(N+1)]
arr[1] = 1

for i in range(2, N+1):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[-1])

# -----------------------------------
# 반복문 이용
def fibo_for(n):
    list=[]
    for i in range(0, n+1):
        if i == 0:
            list.append(0)
        elif i < 2:
            list.append(1)
        else:
            list.append(list[i-1] + list[i-2])
    return list

n = int(input())
print(fibo_for(n)[-1])
# ------------------------------------------


# 재귀함수 이용 --시간초과
def fibo_re(n):
    if n < 3:
        return 1
    else:
        return fibo_re(n-1) + fibo_re(n-2)
