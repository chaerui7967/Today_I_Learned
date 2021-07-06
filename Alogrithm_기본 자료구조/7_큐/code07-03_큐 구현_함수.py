# 함수
# 큐가 꽉찾는지 확인
def isQueueFull():
    global SIZE, queue, front, rear
    if rear != SIZE-1:
        return False
    elif rear == SIZE -1 and front == -1:
        return True
    else:
        for i in range(front-1,SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

# 큐가 비어있는 지
def isQueueEmpty():
    global SIZE, queue, front, rear

    if rear == front:
        return True
    else:
        return False

# 데이터 삽입 enqueue
def enQueue(data):
    global SIZE, queue, front, rear

    if isQueueFull():
        print('큐가 가득참')
        return
    rear += 1
    queue[rear] = data

# 데이터 추출 dequeue
def deQueue():
    global SIZE, queue, front, rear

    if isQueueEmpty():
        print('큐가 빔')
    front += 1
    data = queue[front]
    queue[front] = None
    return data

# 전역변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

# 메인코드
if __name__ == '__main__':
    queue = ['화사', '솔라', '문별', '휘인', '선미']
    front = -1
    rear = 4
    print('현재 큐 : ', queue,'rear : ',rear,'front : ',front)
    print('큐에 빈공간이 없나?', isQueueFull())
    queue = [None for _ in range(SIZE)]
    front = rear = -1
    print('현재 큐 : ', queue, 'rear : ', rear, 'front : ', front)
    print('큐가 비어잇나?', isQueueEmpty())
    print('----데이터 삽입------')
    data = input('삽입할 데이터')
    enQueue(data)
    print('현재 큐 : ', queue, 'rear : ', rear, 'front : ', front)
    print('----데이터 삭제-----')
    print(deQueue())
    print('현재 큐 : ', queue, 'rear : ', rear, 'front : ', front)
    print(deQueue())
    print('현재 큐 : ', queue, 'rear : ', rear, 'front : ', front)
