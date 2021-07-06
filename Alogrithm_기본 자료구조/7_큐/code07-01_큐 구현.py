# 큐 생성, 초기화
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

# 삽입 inqueue
rear += 1
queue[rear] = '화사'
rear += 1
queue[rear] = '솔라'
rear += 1
queue[rear] = '문별'

print(queue)

# 추출 dequeue
front += 1
data = queue[front]
queue[front] = None
print('추출', data)

