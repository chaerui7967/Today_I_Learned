# Bronze 5_3003

# 체스는 총 16개의 피스를 사용하며, 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성되어 있다.
# 동혁이가 발견한 흰색 피스의 개수가 주어졌을 때,
# 몇 개를 더하거나 빼야 올바른 세트가 되는지 구하는 프로그램을 작성하시오.

Chess_co = [1, 1, 2, 2, 2, 8]
white = list(map(int,input().split(' ')))

for i in range(len(Chess_co)):
    print(Chess_co[i] - white[i], end=' ')

# 원래 기본 흰색체스 판의 말 수를 리스트에 넣는다.
# list를 입력받아야하기 때문에 list함수와 input.split 함수를 활용한다
# for문을 활용하여 각 말의 차이를 출력한다.