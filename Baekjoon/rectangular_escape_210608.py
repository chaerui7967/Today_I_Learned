# Bronze 3_1085
# 한수는 지금 (x, y)에 있다. 직사각형의 왼쪽 아래 꼭짓점은 (0, 0)에 있고,
# 오른쪽 위 꼭짓점은 (w, h)에 있다.
# 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

x, y, w, h = map(int, input().split())

if w - x < x:    xd = w - x
else:    xd = x

if h - y < y:    yd = h - y
else:    yd = y

if xd < yd:    print(xd)
else:   print(yd)

