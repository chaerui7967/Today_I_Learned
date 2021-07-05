## 클래스 또는 함수 선언부 ##
# 노드 생성 클래스 생성
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

## 전역 변수 부

memory = []
head, current, pre = None, None, None
# dataArray = ['다현', '정연', '쯔위', '사나', '지효']  # DB, 크롤링 ...
import random
dataArray = [random.randint(1000, 9999) for _ in range(20)]

## 메인 코드 부

if __name__ == '__main__':  # C, Java, C++, C# ==> main()
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)
