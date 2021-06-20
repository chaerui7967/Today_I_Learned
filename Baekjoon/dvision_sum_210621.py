# Bronze 2_2231

# 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다.
# 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다.
# 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다.
# 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다.
# 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.
# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

# 브루트 포스 문제

n = int(input())

for i in range(n + 1):
    i_s = str(i)
    total = i
    for j in i_s:
        total += int(j)
    if total == n:
        break
print(i if i != n else 0)


# 다른방법
n = int(input())
x = 0
for i in range(1, n+1):         # 1부터 n까지
    a = list(map(int, str(i)))  # 각 자리 수를 분해
    s = i + sum(a)              # 분해합을 구함
    if(s == n):                 # 만약 분해합이 n과 같다면
        x = i                   # x = i, 종료
        break

print(x)