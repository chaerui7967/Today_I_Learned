# Silver 5_17626

# 라그랑주는 1770년에 모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현할 수 있다고 증명하였다.
# 어떤 자연수는 복수의 방법으로 표현된다.
# 예를 들면, 26은 52과 12의 합이다.
# 또한 42 + 32 + 12으로 표현할 수도 있다.
# 역사적으로 암산의 명수들에게 공통적으로 주어지는 문제가 바로 자연수를 넷 혹은
# 그 이하의 제곱수 합으로 나타내라는 것이었다.
# 1900년대 초반에 한 암산가가 15663 = 1252 + 62 + 12 + 12라는 해를 구하는데 8초가 걸렸다는 보고가 있다.
# 좀 더 어려운 문제에 대해서는 56초가 걸렸다. 11339 = 1052 + 152 + 82 + 52.
# 자연수 n이 주어질 때, n을 최소 개수의 제곱수 합으로 표현하는 컴퓨터 프로그램을 작성하시오.

n = int(input())
min_sum = 4  # 최대는 4라고 증명되어있다, 아래 3중 for문에서 걸리지 않는다면 답은 4
for a in range(int(n ** 0.5), int((n // 4) ** 0.5), -1):  # 가능한 최소한의 범위로 축소해준다
    if a * a == n:
        min_sum = 1  # 최소의 숫자일 경우
        break
    else:
        temp = n - a * a
        for b in range(int(temp ** 0.5), int((temp // 3) ** 0.5), -1):  # 남은 숫자는 3이니까 3으로 나누어줌
            if a * a + b * b == n:
                min_sum = min(min_sum, 2)
                continue
            else:
                temp = n - a * a - b * b
                for c in range(int(temp ** 0.5), int((temp // 2) ** 0.5), -1):
                    if n == a * a + b * b + c * c:
                        min_sum = min(min_sum, 3)

print(min_sum)



# ======= 간단한 구현

N = int(input())
dp = [0,1]

for i in range(2, N+1):
    min_value = 1e9
    j = 1

    while (j**2) <= i:
        min_value = min(min_value, dp[i - (j**2)])
        j += 1

    dp.append(min_value + 1)
print(dp[N])