# Silver 4_10866

# 정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
#
# 명령은 총 여덟 가지이다.
#
# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다.
#           만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다.
#           만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
arr = deque([])

for i in range(n):
    cmd = list(input().split())
    if cmd[0] == 'push_front':
        arr.insert(0,cmd[1])
    elif cmd[0] == 'push_back':
        arr.append(cmd[1])
    elif cmd[0] == 'pop_front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.popleft())
    elif cmd[0] == 'pop_back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    elif cmd[0] == 'size':
        print(len(arr))
    elif cmd[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif cmd[0] == 'back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])

# ==== 함수로 만들어서 실행
import sys

class dequeue():
    def __init__(self):
        self.my_list = []
        self.size = 0

    def push_front(self, item):
        self.my_list.insert(0, item)
        self.size += 1

    def push_back(self, item):
        self.my_list.append(item)
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            return -1
        else:
            self.size -= 1
            return self.my_list.pop(0)

    def pop_back(self):
        if self.size == 0:
            return -1
        else:
            self.size -= 1
            return self.my_list.pop(-1)

    def my_size(self):
        return self.size

    def empty(self):
        if self.size == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.size == 0:
            return -1
        else:
            return self.my_list[0]

    def back(self):
        if self.size == 0:
            return -1
        else:
            return self.my_list[-1]

if __name__ == '__main__':
    d = dequeue()
    t = int(sys.stdin.readline())
    for _ in range(t):
        command = input().split()
        if command[0] == 'push_back':
            d.push_back(command[1])
        elif command[0] == 'push_front':
            d.push_front(command[1])
        elif command[0] == 'front':
            sys.stdout.write(str(d.front()))
            sys.stdout.write('\n')
        elif command[0] == 'back':
            sys.stdout.write(str(d.back()))
            sys.stdout.write('\n')
        elif command[0] == 'size':
            sys.stdout.write(str(d.my_size()))
            sys.stdout.write('\n')
        elif command[0] == 'empty':
            sys.stdout.write(str(d.empty()))
            sys.stdout.write('\n')
        elif command[0] == 'pop_front':
            sys.stdout.write(str(d.pop_front()))
            sys.stdout.write('\n')
        elif command[0] == 'pop_back':
            sys.stdout.write(str(d.pop_back()))
            sys.stdout.write('\n')
