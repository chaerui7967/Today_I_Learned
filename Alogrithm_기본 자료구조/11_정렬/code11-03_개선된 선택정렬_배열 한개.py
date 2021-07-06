# 함수 선언
def selectionSort(ary):
    n = len(ary)
    for i in range(0,n-1):
        minIdx = i
        for k in range(i+1, n):
            if ary[minIdx] > ary[k]:
                minIdx = k
        ary[i], ary[minIdx] = ary[minIdx], ary[i]
    return ary

# 전역변수
import random
data = [random.randint(50, 190) for _ in range(8)]


# 메인 코드
print('정렬 전', data)

data = selectionSort(data)

print('정렬 후', data)