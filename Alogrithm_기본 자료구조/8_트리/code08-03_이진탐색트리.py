class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


# 전역 변수
memory = []
root = None
# 데이터베이스 또는 크롤링으로 얻은 로우 데이터 집합
nameAry = ['블랙핑크', '레드벨벳', '에이핑크', '걸스데이', '트와이스', '마마무']

# 첫 번째 노드 생성
name = nameAry[0]
node = TreeNode()
root = node
node.data = name
memory.append(node)

# 다음 노드들 생성
for name in nameAry[1:]:
    node = TreeNode()
    node.data = name
    current = root
    while True:
        if name < current.data:
            if current.left == None:
                current.left = node
                break
            else:
                current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right

    memory.append(node)

# 데이터 검색
findName = '마마무'
current = root
while True:
    if current.data == findName:
        print(findName, '찾음')
        break
    elif current.data > findName:
        if current.left == None:
            print('없음')
            break
        current = current.left
    else:
        if current.right == None:
            print('없음')
            break
        current = current.right
