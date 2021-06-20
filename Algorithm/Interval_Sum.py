# 구간 합 문제 : 연속적으로 나열된 n개의 수가 있을 때 특정 구간의 모든 수를 합한 값을 계산하는 문제
# 예를 들어 [10,20,30,40,50]에서 두 번째 수부터 네 번째 수까지의 합은 90

# 구간 합 빠르게 계산
# n개의 정수로 구성된 수열이 있다.
# m개의 쿼리 정보가 주어짐
#     각 쿼리는 left와 right로 구성
#     각 쿼리에 대해 [left, right] 구간에 포함된 데이터들의 합을 출력
#  수행 시간 제한은 O(N + M)

# 해결 아이디어
# 접두사 합(Prefix Sum) :  배열의 맨 앞부터 특정 위치까지의 합을 미리 구해 놓은 것
# 접두사 합을 활용한 알고리즘
#     n개의 수 위치 각각에 대해 접두사 합을 계산하여 P에 저장
#     매 m개의 쿼리 정보를 확인할 때 구간 합은 P[right] - P[left-1]

n = 5
data = [10,20,30,40,50]

# 접두사 합 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간 합 계산
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left-1])

