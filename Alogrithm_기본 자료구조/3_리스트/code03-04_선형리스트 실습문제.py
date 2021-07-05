# 함수 선언
def add_data(friend):

    katok.append(None)
    klen = len(katok)
    katok[klen-1] = friend

def insert_data(friend,position):

    katok.append(None)
    klen = len(katok)

    for i in range(klen-1, position,-1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend

def delet_data(position):

    klen = len(katok)
    katok[position] = None

    for i in range(position + 1, klen):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[klen-1])

# =========================================

katok = []
select = -1

if __name__ == "__main__":
    while select != 4:
        select = int(input('선택 ( 1: 추가, 2: 삽입, 3: 삭제, 4: 종료 )'))

        if select==1:
            data = input('추가할 데이터 : ')
            add_data(data)
            print(katok)
        elif select==2:
            data = input('삽입할 데이터 :')
            pos = int(input('삽입 위치(0부터 시작) :'))
            insert_data(data,pos)
            print(katok)
        elif select==3:
            pos = int(input('삭제할 데이터위치 :'))
            delet_data(pos)
            print(katok)
        elif select==4:
            print(katok)
            break
        else:
            print('1~4중 하나를 고르시오')
            continue