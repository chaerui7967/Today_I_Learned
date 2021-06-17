# Bronze 3_1964

# 오각형이 커지면서 점이찍힌다.
# 첫번째 오각형은 5개
# 두번째 오각형은 12개 ...
# N단계에서 점의 개수는 모두 몇 개일까?

# 입력 N 출력 N단계에서의 점의 개수를 45678로 나눈 나머지 출력

n = int(input())
sum = 1

for i in range(1, n + 1):
    sum = sum + 3 * i + 1

print(sum % 45678)