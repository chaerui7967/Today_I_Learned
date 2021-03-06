# Bronze 3_1009
# 각 컴퓨터에 1번부터 10번까지의 번호를 부여하고,
# 10대의 컴퓨터가 다음과 같은 방법으로 데이터들을 처리하기로 하였다.
#
# 1번 데이터는 1번 컴퓨터, 2번 데이터는 2번 컴퓨터, 3번 데이터는 3번 컴퓨터, ... ,
# 10번 데이터는 10번 컴퓨터, 11번 데이터는 1번 컴퓨터, 12번 데이터는 2번 컴퓨터, ...
#
# 총 데이터의 개수는 항상 ab개의 형태로 주어진다.
# 재용이는 문득 마지막 데이터가 처리될 컴퓨터의 번호가 궁금해졌다.
# 이를 수행해주는 프로그램을 작성하라.

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    a = a % 10  # 마지막 컴퓨터를 찾는 것이므로 1의자리만 보면 된다.
    if a == 0:  # a가 10의 배수인 경우는 무조건 1의 자리가 0이므로 마지막 컴퓨터는 10번째
        print(10)
    elif a == 1 or a == 5 or a == 6:  # 1의 자리가 1, 5, 6이면 제곱들의 자릿수는 1, 5, 6에서 변하지 않는다.
        print(a)

    # 1의 자리 수가 4와 9인 경우는 반복되는 값이 2개 이므로 제곱수를 2로 나누어서
    # 홀수 승과 짝수 승을 비교하여 계산한다
    # 4 -> (1)6 -> (2)4
    # 9 -> (8)1 -> (72)9
    elif a == 4 or a == 9:
        b = b % 2
        if b == 1:
            print(a)
        else:
            print((a * a) % 10)
    # 4개씩 싸이클을 돌 때 마다 자기 자신이 나오므로 나누었을 때 0이면 자기자신을 출력
    else:
        b %= 4
        if b == 0:
            print((a ** 4) % 10)
        else:
            print((a ** b) % 10)

