# 서로소 집합은 공통 원소가 없는 두 집합을 의미
# 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료 구조
# 합집합 = 두 개의 원소가 포함된 집합을 하나의 집합으로 합침
# 찾기 = 특정한 원소가 속한 집합이 어떤 집합인지 알려줌
# 합치기 찾기 자료구조라고도 함 (유니온 파인드)

# union
# 1. 해당 노드의 루트 노드를 찾음
# 2. 더 작은 루트 노드를 큰 노드의 루트노드로 설정

# 합집합 연산이 편향되게 이루어지는 경우 찾기 함수가 비효율적으로 동작
# 최악의 경우 찾기 함수가 모든 노드를 다 확인하게 되어서 시간 복잡도 O(V)가 된다

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력
v, e = map(int, input().split())
parent = [0] * (v + 1)

# 부모 테이블상에서, 부모를 자기자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# union 연산 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합 : ', end=' ')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블 : ', end= ' ')
for i in range(1,v+1):
    print(parent[i], end=' ')