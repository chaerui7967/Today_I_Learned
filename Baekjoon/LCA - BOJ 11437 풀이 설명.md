LCA - BOJ 11437 풀이 설명



**접근**

LCA는 두 개의 정점이 공통으로 갖는 조상을 찾는 것이다. 트리는 사이클이 없는 구조이기 때문에 최소 공통 조상을 찾는다면 두 개의 정점의 최단 거리를 구할 수 있게 된다.

 

LCA를 위한 알고리즘을 다른 사이트를 참고하면서 공부를 많이했는데 한 번에 쉽게 이해되지 않았다.

현재까지 이해한 것은 다음과 같다.

\1. LCA를 위해서 세그먼트 트리와 DP를 적용시킬 수 있다. 그 중 DP에 대한 방법을 공부하였다.

\2. 트리를 양방향으로 만들어준다. (일단 지금까지 왜 양방향으로 만들어줘야하는지 알지 못한다.)

\3. 각 정점의 깊이와 첫 번째 부모를 어떠한 리스트에 저장해둔다. 깊이를 구하는 것은 두 개의 정점이 깊이가 다를 때 깊이를 맞춰준 후에 동시에 위로 올라가면서 부모를 찾기위함이다. 또한 첫번째 부모를 찾는 것은 두 개의 정점이 동시에 거슬러올라갈 때 부모가 같은지 검사하기위해 사용한다.

\4. 첫 번째 부모를 구했다면 이를 활용하여 첫 번째 부모의 부모, 부모의 부모의 부모를 통해 루트까지의 부모를 구하고 저장한다.

\5. 이제 깊이가 다르다면 깊이를 맞춰주도록 한다. 

\6. 이후 동시에 거슬러 올라가면서 같은 부모가 나왔을 때 최소 공통 조상으로 정한다.

 

**구현**

정점들의 깊이와 바로 위에있는 첫 번째 부모를 각각 depth와 parent라는 리스트에 저장한다.

```
def dfs(cur, d):
    depth[cur] = d
    visited[cur] = True

    for child in tree[cur]:
        if not visited[child]:
            parent[child][0] = cur
            dfs(child, d+1)
```

 

이제 루트까지 거슬러 올라가면서 부모들을 찾는다. 

현재 정점의 i번째 부모는 i-1번째 부모의 부모이다. 

```
def find_parent():
    for i in range(1, 21):
        for j in range(1, V+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]
```

 

lca함수에서 최소 공통 조상을 찾는다.

먼저 깊이를 맞춰주도록 한다.

b와 a 정점의 높이가 0이 될 때까지 더 깊이있는 정점의 위치를 갱신시킨다.

 

이후 같은 높이에 있을 때 루트까지 거슬러 올라가면서 같은 부모를 찾도록 한다.

```
def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a
    for i in range(20, -1, -1):
        if depth[b] - depth[a] >= (1<<i):
            b = parent[b][i]

    if a == b:
        return b

    for i in range(20, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]
```

------

**전체 코드**

```
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def dfs(cur, d):
    depth[cur] = d
    visited[cur] = True

    for child in tree[cur]:
        if not visited[child]:
            parent[child][0] = cur
            dfs(child, d+1)

def find_parent():
    for i in range(1, 21):
        for j in range(1, V+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a
    for i in range(20, -1, -1):
        if depth[b] - depth[a] >= (1<<i):
            b = parent[b][i]

    if a == b:
        return b

    for i in range(20, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]

def traversal(node):
    global answer

    answer += 1
    for i in tree[node]:
        traversal(i)



V = int(input())
tree = [[] for _ in range(V+1)]
for _ in range(V-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

depth = [0] * (V+1)
parent = [[0 for _ in range(21)] for _ in range(V+1)]
visited = [False] * (V+1)



dfs(1, 0)
find_parent()
M = int(input())
for _ in range(M):
    A, B = map(int, input().split())
    common_parent = lca(A, B)
    print(common_parent)
```



출처 https://kimmeh1.tistory.com/258