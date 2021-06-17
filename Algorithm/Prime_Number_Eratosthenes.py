# 에라토스테네스의 체
# 특정한 수의 범위 안에 존재하는 모든 소수를 찾기
# N보다 작거나 같은 모든 소수를 찾음
# 시간복잡도 O(NloglogN)
# 하지만 각 자연수에 대한 소수 여부를 저장해야 하므로 메모리를 많이 사용

# 1. 2부터 N까지 모든 자연수를 나열
# 2. 남은 수 중에 아직 처리하지 않은 가장 작은 수 i를 찾음
# 3. 남은 수 중에서 i의 배수를 모두 제거
# 4. 더 이상 반복할수 없을 때까지 반복

import math

n = 1000  # 2부터 1000까지 모든 수에 대해 소수 판별
# 처음엔 모든 수가 소수(true)인 것으로 초기화 (0,1제외)
array = [True for i in range(n+1)]

# 에라토스테네스의 체
# 2부터 n의 제곱근까지의 모든 수를 확인
for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True:  # i가 소수인 경우
        # i를 제외한 i의 모든 배수를 삭제
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1
# 모든 소수 출력
for i in range(2,n+1):
    if array[i]:
        print(i, end=' ')
