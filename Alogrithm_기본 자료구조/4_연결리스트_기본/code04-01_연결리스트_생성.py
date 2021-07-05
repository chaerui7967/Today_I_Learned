
# 노드 생성 클래스 생성
class Node():
    def __init__(self):
        self.data = None
        self.link = None

node1 = Node()
node1.data = '다현'

node2 = Node()
node2.data = '정연'
node1.link = node2

# print(node1.data, end=' ')
# print(node1.link.data)

# 간단 구현
current = node1
print(current.data, end =' ')

while current.link != None:
    current = current.link
    print(current.data,end=' ')

# 삽입 구현
newnode = Node()
newnode.data = 'ssss'
newnode.link = node2.link
node2.link = newnode
