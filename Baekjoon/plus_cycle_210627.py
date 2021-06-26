# Bronze 1_1110
# 0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다.
# 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다.
# 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면
# 새로운 수를 만들 수 있다. 다음 예를 보자.
# 26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다.
# 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.
# 위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.
# N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

num = int(input())
check = num
new_num = 0
temp = 0
count = 0
while True:
    # 주어진 수가 1의 자리 수 일 때 어짜피 0을 더해서 풀어도 0 + n = n 이므로 무시해준다
    temp = num // 10 + num % 10
    # 두 자리 수를 각 자리의 숫자로 더한다는 것은 10으로 나눈 몫(10의자리) + 10으로 나눈 나머지(1의자리) 가 된다
    new_num = (num % 10)*10 + temp % 10
    # 새로운 수는 기존 1의자리의 수가 10의 자리로가고 각 자리의 숫자로 더한 수의 1의자리 수와 합친값과 같다
    count += 1
    num = new_num
    if new_num == check:
        break
print(count)