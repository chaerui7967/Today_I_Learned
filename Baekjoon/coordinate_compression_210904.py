# Silver 2_18870

# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

# ======== 풀이
# set함수를 통해 중복을 없애준 후
# 정렬시킨 새로운 리스트를 만들어 준 후에
# arr를 순서대로 돌면서 새로만든 arr2에서 해당 값의 인덱스를 뽑아주면 되는 문제
# list.index(i) 형태의 시간 복잡도 = O(N)
# index[i] 형태의 시간 복잡도 = O(1)

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))
dic = {arr2[i] : i for i in range(len(arr2))}
for i in arr:
    print(dic[i], end = ' ')