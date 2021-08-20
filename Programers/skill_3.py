# Q1
# - 명령어가 'I 숫자'인 경우 명령어의 첫번째 값(o[0])이 I라면 힙에 숫자(o[1])를 저장한다.
#  - 명령어가 ' D 1'인 경우 힙에서 최대값을 삭제한다.이 코드에서 힙이 최소힙으로 되어있기
# 때문에 pop을 하면 최소값이 삭제된다.따라서 최대값을 삭제하기 위해서는
# 힙에서 nlargest()를 사용하여 최대값을 구한 후 최대값의
# 위치를 찾아 그 위치에 있는 값을 삭제하면 된다.

# - 명령어가 'D -1'인 경우 힙에서 최소값을 삭제한다.
#  최소힙이므로 힙에서 pop을 하면 최소값이 삭제된다.
# 마지막으로 최대값, 최소값을 리턴

import heapq


def solution(operations):
    heap = []

    for operation in operations:
        o = operation.split(' ')  # 명령어 값 분리하여 저장

        # 명령어에 따라 처리하는 부분
        if o[0] == 'I':
            heapq.heappush(heap, int(o[1]))  # 명령어가 'I 숫자'인 경우
        else:
            if len(heap) > 0:
                # 명령어가 'D 1'인 경우
                if o[1] == '1':
                    heap.pop(heap.index(heapq.nlargest(1, heap)[0]))
                # 명령어가 'D -1'인 경우
                else:
                    heapq.heappop(heap)

    # 최대값, 최소값 리턴
    if heap:
        return [heapq.nlargest(1, heap)[0], heapq.nsmallest(1, heap)[0]]
    else:
        return [0, 0]