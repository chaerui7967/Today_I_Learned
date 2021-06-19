# 효율적인 화폐 구성
# n가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 m원이 되도록 하려고한다.
# 이때 각 종류의 화폐는 몇 개라도 사용가능하다.
# m원을 만들기 위한 최소한의 화폐 개수를 출력하는 프로그램을 작성하시오.

# ai = 금액 i를 만들 수 있는 최소한의 화폐 개수
# k = 각 화폐의 단위
# 점화식 : 각 화폐 단위인 k를 하나씩 확인하면서
#     ai-k를 만드는 방법이 존재하는 경우, ai = min(ai,ai-k+1)
#     ai-k를 만드는 방법이 존재하지 않는 경우, ai = INF

n, m = map(int,input().split())
# n개의 화폐 단위 정보를 입력
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍 진행(보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001: # (i-k)원을 만들 수 있다면
            d[j] = min(d[j], d[j - array[i]] + 1)
# 계산된 결과 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])

# 입력 예시                      출력
# 2 15                            5
# 2
# 3
#
# 3 4                             -1
# 3
# 5
# 7