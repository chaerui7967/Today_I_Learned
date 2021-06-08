# Bronze 3_1837
# 두 소수 p, q 중 하나라도 K보다 작은 암호는 좋지 않은 암호로 간주하여 제출하지 않기로 하였다.
# 당신은 원룡이를 도와 두 소수의 곱으로 이루어진 암호와 K가 주어져 있을 때,
# 그 암호가 좋은 암호인지 좋지 않은 암호인지 구하는 프로그램을 작성하여야 한다.
# 만약에 그 암호가 좋은 암호이면 첫째 줄에 GOOD을 출력하고,
# 만약에 좋지 않은 암호이면 BAD와 소수 r을 공백으로 구분하여 출력하는데
# r은 암호를 이루는 두 소수 중 작은 소수를 의미한다

P, K = map(int, input().split())
li = [1]*K
for i in range(2, int(K**0.5)+1):
    if li[i] == 1:
        for j in range(i+i, K, i):
            li[j] = 0
prime = [i for i in range(2, K) if li[i] == 1]

good, bad = 1, 0
for n in prime:
    if P%n == 0:
        good, bad = 0, n
        break
print("GOOD" if good else f"BAD {bad}")

# 결국 k보다 작은 소수 값들을 구하여서 p에 나누어보고 만약 나누어진다면 'BAD'와 해당 소수를 출력

# 에라토스테네스의 체를 사용한다
# 에라토스테네스의 채란
# 수가 수(N이라고 가정)를 나누면 몫이 생기는데,
# 몫과 나누는 수 둘 중 하나는 N 제곱근 이하이기 때문이다.