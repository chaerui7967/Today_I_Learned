# Bronze 1_1357

# 어떤 수 X가 주어졌을 때, X의 모든 자리수가 역순이 된 수를 얻을 수 있다.
# Rev(X)를 X의 모든 자리수를 역순으로 만드는 함수라고 하자.
# 예를 들어, X=123일 때, Rev(X) = 321이다. 그리고, X=100일 때, Rev(X) = 1이다.
# 두 양의 정수 X와 Y가 주어졌을 때, Rev(Rev(X) + Rev(Y))를 구하는 프로그램을 작성하시오.

def rev(x):
    x = list(x)
    x.reverse()
    result = 0
    for i in range(len(x)):
        result += int(x[i]) * (10 ** (len(x)-1-i))
    return result

x, y = input().split()
print(rev(str(rev(x) + rev(y))))
