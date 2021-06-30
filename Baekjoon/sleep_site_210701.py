# Bronze 1_1652

# 코레스코 콘도에 있는 방은 NxN의 정사각형모양으로 생겼다.
# 방 안에는 옮길 수 없는 짐들이 이것저것 많이 있어서 영식이의 누울 자리를 차지하고 있었다.
# 영식이는 이 열악한 환경에서 누울 수 있는 자리를 찾아야 한다. 영식이가 누울 수 있는 자리에는 조건이 있다.
# 똑바로 연속해서 2칸 이상의 빈 칸이 존재하면 그 곳에 몸을 양 옆으로 쭉 뻗으면서 누울 수 있다.
# 가로로 누울 수도 있고 세로로 누울 수도 있다.
# 누울 때는 무조건 몸을 쭉 뻗기 때문에 반드시 벽이나 짐에 닿게 된다.
# (중간에 어정쩡하게 눕는 경우가 없다.)
# ....X
# ..XX.
# .....
# .XX..
# X....
# 만약 방의 구조가 위의 그림처럼 생겼다면, 가로로 누울 수 있는 자리는 5개이고,
# 세로로 누울 수 있는 자리는 4개 이다. 방의 크기 N과 방의 구조가 주어졌을 때,
# 가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리의 수를 구하는 프로그램을 작성하시오.

n = int(input())
s = []
cnt_w = 0
cnt_h = 0
position_w = 0
position_h = 0
for i in range(n):
    s.append(input())
for i in s:
    for j in i:
        if j == '.':
            cnt_w += 1
        else:
            if cnt_w > 1:
                position_w += 1
            cnt_w = 0
    if cnt_w > 1:
        position_w += 1
    cnt_w = 0
for i in range(n):
    for j in range(n):
        if s[j][i] == '.':
            cnt_h += 1
        else:
            if cnt_h > 1:
                position_h += 1
            cnt_h = 0
    if cnt_h > 1:
        position_h += 1
    cnt_h = 0
print(position_w, position_h)
