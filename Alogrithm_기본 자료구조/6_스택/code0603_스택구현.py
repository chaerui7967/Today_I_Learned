def isStackFull():
    global SIZE, stack, top
    if top >= SIZE-1:
        return True
    else:
        return False

def isStackEmpty():
    global SIZE, stack, top
    if top == -1:
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if isStackFull():
        print('불가')
        return
    top += 1
    stack[top] = data

def pop():
    global SIZE, stack, top

    if isStackEmpty():
        return print('empty')
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return print(data)

SIZE = 5
stack = ['커피','녹차','꿀물','콜라', None]
top = 3
# stack의 상황 확인
# stack = [None for _ in range(SIZE)]
# top = -1
# print('스택 사용가능?', isStackFull())

# data push
# print(stack)
# push('사이다')
# print(stack)
# push('환타')
# print(stack)

# data pop
pop()
print(stack)
stack = [None]
top = -1
pop()