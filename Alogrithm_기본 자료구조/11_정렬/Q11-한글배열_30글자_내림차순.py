def findMaxIdx(ary):
    maxIdx = 0
    for i in range(1,len(ary)):
        if ary[maxIdx] < ary[i]:
            maxIdx = i
    return maxIdx


# 전역변수
from random import randint
arr = [randint(ord('가'), ord('힣')) for _ in range(30)]
after = []
print('정렬 전 ', arr)
for _ in range(len(arr)):
    maxPos = findMaxIdx(arr)
    after.append(chr(arr[maxPos]))
    del(arr[maxPos])

print('정렬 후', after)