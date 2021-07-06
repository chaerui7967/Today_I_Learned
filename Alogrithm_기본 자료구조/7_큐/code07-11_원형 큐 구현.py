# 함수 선언
# 큐가 비어있는 지
def isQueueEmpty():
    global SIZE, queue, front, rear
    if rear == front:
        return True
    else:
        return False

# 큐가 가득찼는 지
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear+1) % SIZE == front:
        return True
    else:
        return False

# enqueue
def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        return print('큐가 가득참')
    rear = (rear+1) % SIZE
    queue[rear] = data

# dequeue
def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        return print('큐가 비어있음')
    front = (front+1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

# 전역 변수

SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0

# 메인

enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('현재 큐 : ', queue, 'rear : ', rear, 'front : ', front)
print(deQueue())
print(deQueue())
print('현재 큐 : ', queue, 'rear : ', rear, 'front : ', front)
enQueue('길호')
print('현재 큐 : ', queue, 'rear : ', rear, 'front : ', front)

