# 함수 선언
def binSearch(ary,data):
    pos = -1
    start = 0
    end = len(ary) - 1

    while start <= end:
        mid = (start+end)//2
        if data == ary[mid]:
            return mid
        elif data > ary[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return pos

# 전역 변수 선언
dataAry = [50,60,105,120,150,160,162,168,177,188]
findData = 162

# 메인 코드
print('배열 : ',dataAry)
position = binSearch(dataAry,findData)
if position == -1:
    print('값 없음')
else:
    print(position,'번째')