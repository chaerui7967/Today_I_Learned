# 파라메트릭 서치
# 최적화 문제를 결정 문제(예, 아니오)로 바꾸어 해결하는 기법
#   특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
# 이진탐색을 이용하여 해결

# 예시 문제
# 높이가 19,14,10,17 인 떡이 나란히 있고 절단기 높이를 15로 지정하면 자른뒤 떡의높이는 15,14,10,15
# 가 된다. 잘린 떡의 길이는 4,0,0,2 이다
# 손님은 6만큼의 길이를 가져감
# 손님이 왔을 때 요청한 총 길이가 m일 때 적어도 m만큼의 떡을 얻기 위해
# 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성

n,m = list(map(int, input().split()))
# 떡의 개별 높이 정보 입력
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복)
result = 0
while(start<=end):
    total = 0
    mid = (start+end)//2
    for x in array:
        # 잘랐을 때의 떡의 양
        if x> mid:
            total += x-mid
    # 떡의 양이 부족한 경우
    if total < m:
        end = mid -1
    # 떡의 양이 충분
    else:
        result = mid
        start = mid+1
print(result)

# n개의 원소를 포함하고 있는 수열이 오름차순으로 정렬
# 이때 이 수열에서 x가 등장하는 횟수를 계산
# 예를들어 [1,1,2,2,2,2,3] 이 있을 때 x=2라면, 현재 수열에서 값이 2인 원소가 4개 이므로 4 출력
# 시간복잡도는 O(logN) 선형탐색은 시간초과
# 순열은 기본적으로 오름차순으로 작성

from bisect import bisect_left,bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

n,x = map(int,input().split())
array = list(map(int,input().split()))

# 값이 [x,x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array,x,x)

# 값이 x인 원소가 존재하지 않으면
if count ==0 :
    print(-1)
# 값이 x인 원소가 존재
else:
    print(count)