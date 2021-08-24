# Silver 2_11047

# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
#
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

n, k = map(int, input().split())
coin = []
num = 0

for _ in range(n):
    coin.append(int(input()))

for i in range(n -1, -1, -1):
    if k == 0:
        break
    if coin[i] > k:
        continue
    num += k // coin[i]
    k %= coin[i]
print(num)