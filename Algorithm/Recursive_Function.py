# 재귀 함수 = 자기 자신을 다시 호출하는 함수
# 종료 조건을 반드시 명시
# 유의 사항
# 오히려 다른 사람이 이해하기 어려운 형태가 될 수 있으므로 신중하게 사용
# 모든 재귀함수는 반복문을 이용하여 동일하게 구현가능
# 반복문이 더 유리한 경우도 있음
# 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓임
#     그래서 스택을 사용해야 할 때 구현상 스택 라이브러리 대신에 재귀함수를 사용하는 경우가 많음

def recursive_function(i):
    # 100번째 호출 했을 때 종료
    if i == 100:
        return
    print(f'{i}번째에서 {i+1}번째 호출')
    recursive_function(i+1)
    print(f'{i}번째 종료')

# 팩토리얼 구현

def factorial_iterative(n):
    result = 1
    # 1부터 n까지 수를 차례대로 곱
    for i in range(1,n+1):
        result *= i
    return result

# 재귀적으로 구현
def factorial_recursive(n):
    if n<= 1:  # n이 1 이하인 경우 1
        return 1
    # n! = n * (n-1)!
    return n * factorial_recursive(n-1)

print('반복구현 : ', factorial_iterative(5))
print('재귀구현 : ', factorial_recursive(5))

# 최대 공약수 계산 (유클리드 호제법)
# 두 자연수 a,b 에 대하여 a>b에서 a를 b로 나눈 나머지를 r이라고 할때
# a와 b의 최대공약수는 b와 r의 최대공약수와 같다
# GCD(192, 162)
# 1. 192 162
# 2. 162 30
# 3. 30 12
# 4. 12 *6*

def gcd(a,b):
    if a%b ==0:
        return b
    else:
        return gcd(b, a%b)

print(gcd(192,162))
