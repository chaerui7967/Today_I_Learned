# 소수 판별 알고리즘

# 간단 구현
def is_prime_number(x):
    # 2부터 (x-1)까지의 모든 수를 확인
    for i in range(2,x):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False
    return True
# 성능은 시간복잡도 O(X)가 됨

# 약수의 성질
# 모든 약수가 가운데 약수를 기준으로 곱셈 연산에 대해 대칭을 이룸
# 예를 들어 16의 약수는 1,2, * 4 * ,8,16
# 따라서 특정한 자연수의 모든 약수를 찾을 때 가운데 약수(제곱근)까지만 확인하면 됨

# 개선 알고리즘
# 시간 복잡도 O(N**0.5)
import math

def is_prime_number1(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

