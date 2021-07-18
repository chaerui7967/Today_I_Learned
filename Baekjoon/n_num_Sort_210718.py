# Silver 5_2751

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 시간 복잡도가 O(NlogN) 까지 가능 log2N = 10 이면 2^10 = 1024≈103 이므로, log2N = 20
# 정도일 때 N≈106 이다.이 복잡도는 1초에 약 2천만번의 연산 횟수 가능

# ====== 병합 정렬 사용
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array


# 데이터 입력
n = int(input())
num = []

for _ in range(n):
    num.append(int(input()))

num = merge_sort(num)

for i in num:
    print(i)


# ===== 내장 함수 사용
n = int(input())
num = []
for i in range(n):
    num.append(int(input()))

for i in sorted(num):
    print(i)
