# 함수
def selectSort(arr):
    n = len(arr)
    for i in range(n-1):
        maxIdx = i
        for j in range(i+1,n):
            if arr[maxIdx] < arr[j]:
                maxIdx = j
        arr[maxIdx], arr[i] = arr[i], arr[maxIdx]
    return arr

# 전역 변수
from random import randint
arr = [chr(randint(ord('가'), ord('힣'))) for _ in range(30)]

print('정렬 전 ', arr)

arr = selectSort(arr)

print('정렬 후', arr)