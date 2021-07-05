# 클래스 함수 선언 부

class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNode(start):
    current = start
    print(current.data, end=' ')

    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData):

    global memory, head, current, pre

    if head == findData:
        node = Node()
        node.data = insertData
        node.link = head.link
        head = node
        return
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
    node = Node()
    node.data = insertData
    current.link = node

def deleteNode(deleteData):
    global memory, head, current, pre

    if head.data == deleteData:
        current = head
        head = head.link
        del(current)
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link

        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return

# 전역 변수부
memory = []
head, current, pre = None, None, None

import random
dataArray = [ random.randint(1000, 9999) for _ in range(20)]

# 메인 코드

if __name__ == '__main__':
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

# 출력확인
printNode(memory[0])

insertNode(memory[2].data, 11111111111111)

printNode(memory[0])

deleteNode(memory[0].data)

printNode(memory[0])