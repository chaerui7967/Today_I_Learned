class Graph():
    def __init__(self, size):
        self.Size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

g1, g2 = None, None

# 메인 코드

g1 = Graph(4)
g1.graph[0][1] = 1
g1.graph[0][2] = 1
g1.graph[0][3] = 1
g1.graph[1][0] = 1
g1.graph[1][2] = 1
g1.graph[2][0] = 1
g1.graph[2][1] = 1
g1.graph[2][3] = 1
g1.graph[3][0] = 1
g1.graph[3][2] = 1

print('g1 무방향 그래프')
for row in range(4):
    for col in range(4):
        print(g1.graph[row][col], end=' ')
    print()

print('g2 방향 그래프')
g2 = Graph(4)
g2.graph[0][1] = 1
g2.graph[0][2] = 1
g2.graph[3][0] = 1
g2.graph[3][2] = 1
for row in range(4):
    for col in range(4):
        print(g2.graph[row][col], end=' ')
    print()