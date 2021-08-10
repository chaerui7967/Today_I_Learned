# Silver 3_1003

# fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.
#
# fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
# fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
# 두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
# fibonacci(0)은 0을 출력하고, 0을 리턴한다.
# fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
# 첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
# fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.

# 1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때,
# 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.
# 제한시간 0.25초, 메모리 제한 128mb

# 다이나믹 프로그래밍을 통해서 이전 숫자를 더해서 답을 나타낼 수 있다
# 해당 문제의 0의 수와 1의 수의 순서도 피보나치 수와 같은 규칙으로 증가한다.

zero = [1, 0, 1]
one = [0, 1, 1]

def fibonacci(num):
    length = len(zero)
    if num >= length:  # 저장되있지 않은 수이면
        for i in range(length, num + 1):
            zero.append(zero[i - 1] + zero[i - 2])  # 마지막 숫자 다음부터 해당 수까지 저장
            one.append(one[i - 1] + one[i - 2])
    print('{} {}'.format(zero[num], one[num]))

T = int(input())

for _ in range(T):
    fibonacci(int(input()))