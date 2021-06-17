# 이진 탐색 알고리즘
# 순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인
# 이진 탐색 : 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색
#   이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색범위를 설정

# 단계마다 탐색범위를 2로 나누는 것과 동일하기 때문에 연산횟수는 logN에 비례
# 시간 복잡도는 O(logN)

# 재귀함수를 이용한 이진 탐색
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) //2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자하는 값이 작은경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    # 중간점의 값보다 클 때 오른쪽 반환
    else:
        return binary_search(array,target,mid+1,end)

# n(원소의 개수), target(찾고자 하는 값) 입력
n, target = list(map(int,input().split()))
# 전체 원소 입력
array = list(map(int,input().split()))

# 이진 탐색 수행 결과
result = binary_search(array,target, 0 ,n-1)
if result == None:
    print('x')
else:
    print(result + 1)

# 반복문 구현
def binary_search1(array, target, start, end):
    while start<= end:
        mid = (start + end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

# n(원소의 개수), target(찾고자 하는 값) 입력
n, target = list(map(int,input().split()))
# 전체 원소 입력
array = list(map(int,input().split()))

# 이진 탐색 수행 결과
result = binary_search1(array,target, 0 ,n-1)
if result == None:
    print('x')
else:
    print(result + 1)

