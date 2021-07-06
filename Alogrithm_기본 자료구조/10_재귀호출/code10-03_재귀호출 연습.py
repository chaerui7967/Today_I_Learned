def addNumber(num):
    if num <= 1:
        return 1
    return num + addNumber(num-1)

# 팩토리얼 구현
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)

# 카운트 다운
def countDown(n):
    if n == 0:
        print('발사')
    else:
        print(n)
        countDown(n-1)

# 별모양 출력
def printStar(n):
    if n > 0:
        printStar(n-1)
        print('*'*n)

# 구구단
def gugu(dan,num):
    print(f'{dan} * {num} = {dan*num}')
    if num < 9:
        gugu(dan, num+1)

# 제곱 계산
def pow(x,n):
    if n == 0:
        return 1
    return x*pow(x,n-1)

# 배열 합
import random

def arysum(arr,n):
    if n <= 0:
        return arr[0]
    return arysum(arr,n-1) + arr[n]

# 전역 변수
arr = [random.randint(0, 255) for _ in range(random.randint(10,20))]


# 메인 함수
print(addNumber(10))
print(factorial(5))
countDown(10)
printStar(5)
gugu(2,1)
print(pow(2,4))

print(arr)
print('arr 합계',arysum(arr,len(arr)-1))