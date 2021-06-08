# 정렬 알고리즘 2

# 퀵 정렬
# 시간복잡도 O(nlogn), 최악의 경우 O(n^2) = 이미 정렬된 경우

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return
    pivot = start  # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):  # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right):  # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 가각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

# 다른 방법
array2 = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort2(array):  # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0]  # 피벗은 첫 번째 원소
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

print(quick_sort2(array2))


# 계수 정렬
# 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용가능
# 동일한 값을 가지는 데이터가 있을 때 효율적
# 데이터 범위가 클 때는 비효율적 ex) [0, 99999999]
# 데이터 개수가 n, 데이터 중 최댓값이 k일 때 최악의 경우에도 시간복잡도가 O(n+k)
# 해당 데이터가 몇번 증가했는지 확인

# 모든 원소의 값이 0보다 크거나 같다고 가정
array3 = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array3) + 1)

for i in range(len(array3)):
    count[array3[i]] += 1  # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):  # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ')  # 등장한 횟수 출력
