# Bronze 2_1408

# 임무를 시작한지 정확하게 24시간이 되는 순간에 잡으려고 한다.
# 만약 지금 시간이 13:52:30이고, 임무를 시작한 시간이 14:00:00 이라면 도현이에게 남은시간은 00:07:30 이다.
# 모든 시간은 00:00:00 ~ 23:59:59로 표현할 수 있다.
# 입력과 출력에 주어지는 모든 시간은 XX:XX:XX 형태이며, 숫자가 2자리가 아닐 경우에는 0으로 채운다.
# 도현이가 임무를 시작한 시간과, 현재 시간이 주어졌을 때, 도현이에게 남은 시간을 구하는 프로그램을 작성하시오.

t = []
s = input().split(":")
t.append(int(s[0])*3600 + int(s[1])*60 + int(s[2]))
s = input().split(":")
t.append(int(s[0])*3600 + int(s[1])*60 + int(s[2]))

if len(t) == 1:
    t.append(t[0])
elif t[0] <= t[1]:
    t[0] += 86400

sec = 86400 - (t[0] - t[1])
time = []
time.append(str("%02d" %(sec//3600)))
sec %= 3600
time.append(str("%02d" %(sec//60)))
sec %= 60
time.append(str("%02d" %(sec)))
print(":".join(time))