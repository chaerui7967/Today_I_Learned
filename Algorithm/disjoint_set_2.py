# 서로소 집합
# 합집합 연산이 편향되게 이루어지는 경우 찾기 함수가 비효율적으로 동작
# 최악의 경우 찾기 함수가 모든 노드를 다 확인하게 되어서 시간 복잡도 O(V)가 된다

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):  # find 함수 수정(경로 압축)
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

# 경로 압축기법을 적용하면 각 노드에 대하여 루트 노드가 바로 루트노드가 됨

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