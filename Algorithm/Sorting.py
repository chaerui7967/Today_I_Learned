# 정렬 알고리즘

# 선택 정렬
# 시간복잡도 O(n^2)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 스와프

print(array)

# 삽입 정렬
# 시간 복잡도 O(n^2)
# 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 작동
# 최선의 경우(이미 정렬이 되어있을 때) 시간복잡도 O(n)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):  # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j-1]:  # 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else:  # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
print(array)
