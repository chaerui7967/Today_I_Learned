# Bronze 1_1924

# 오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까?
# 이를 알아내는 프로그램을 작성하시오.

a=['SUN','MON','TUE','WED','THU','FRI','SAT']
b=[31,28,31,30,31,30,31,31,30,31,30,31]

x,y = map(int,input().split())
day = 0
for i in range(x-1):
    day += b[i]

day = (day+y) % 7
print(a[day])

# calendar module 사용
import calendar

arrList = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
x, y = map(int,input().split())

Day = calendar.weekday(2007, x, y)
print(arrList[Day])