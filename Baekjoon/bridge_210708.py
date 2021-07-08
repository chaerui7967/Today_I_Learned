# Silver 5_1010

# 주변에서 다리를 짓기에 적합한 곳을 사이트라고 한다.
# 재원이는 강 주변을 면밀히 조사해 본 결과 강의 서쪽에는 N개의 사이트가 있고
# 동쪽에는 M개의 사이트가 있다는 것을 알았다. (N ≤ M)
# 재원이는 서쪽의 사이트와 동쪽의 사이트를 다리로 연결하려고 한다.
# (이때 한 사이트에는 최대 한 개의 다리만 연결될 수 있다.)
# 재원이는 다리를 최대한 많이 지으려고 하기 때문에 서쪽의 사이트 개수만큼 (N개) 다리를 지으려고 한다.
# 다리끼리는 서로 겹쳐질 수 없다고 할 때 다리를 지을 수 있는 경우의 수를 구하는 프로그램을 작성하라.


# 조합을 사용하면 구할수 있다 mCn
T = int(input())

for _ in range(T):
    m, n = map(int, input().split())
    answer = 1
    k = n - m

    while n > k:
        answer *= n
        n -= 1
    while m > 1:
        answer = answer // m
        m -= 1

    print(answer)

# =========재귀호출 펙토리알 사용 ==> 런타임 오류

def fac(num):
    if num == 1:
        return 1
    return num * fac(num-1)

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    result = fac(m) / (fac(m-n)*fac(n))
    print(result)


