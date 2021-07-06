def openBox():
    global count
    print('박스 열기')
    count -= 1
    if count == 0:
        print('-'*5, '반지 넣기', '-'*5)
        return
    openBox()
    print('박스 닫음')

# 전역 변수
count = 10

# 메인 함수 수행
openBox()