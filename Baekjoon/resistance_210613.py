# Bronze 2_1076
# 전자 제품에는 저항이 들어간다. 저항은 색 3개를 이용해서 그 저항이 몇 옴인지 나타낸다.
# 처음 색 2개는 저항의 값이고, 마지막 색은 곱해야 하는 값이다.
# 저항의 값은 다음 표를 이용해서 구한다.

# 색	값	곱
# black	0	1
# brown	1	10
# red	2	100
# orange	3	1000
# yellow	4	10000
# green	5	100000
# blue	6	1000000
# violet	7	10000000
# grey	8	100000000
# white	9	1000000000
# 예를 들어, 저항에 색이 yellow, violet, red였다면 저항의 값은 4,700이 된다.

color = ['black', 'brown', 'red',
'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
f = color.index(input())
s = color.index(input())
t = color.index(input())
r = int(str(f) + str(s)) * (10 ** t)
print(r)