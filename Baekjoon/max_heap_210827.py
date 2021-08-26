# Silver 2_11279

# 널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.
#
# 배열에 자연수 x를 넣는다.
# 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

# ===== heapq는 최소 힙만 지원 따라서 음수로 변환하여 최솟값을 추출 후 양수로 다시 변환
import sys
import heapq

n = int(input())
hp = []

for _ in range(n):
    a = int(sys.stdin.readline())
    if a != 0:
        heapq.heappush(hp, (-a))
    else:
        try:
            print(-1 * heapq.heappop(hp))
        except:
            print(0)

# ====== 그냥 해봤지만 역시나 시간초과

n = int(input())
hp = []

for _ in range(n):
    a = int(input())
    hp.append(a)
    if a == 0:
        if len(hp) == 0:
            print(0)
        else:
            print(max(hp))
            hp.pop(hp.index(max(hp)))
