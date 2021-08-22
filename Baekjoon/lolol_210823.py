# Silver 2_5525

# N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.
#
# P1 IOI
# P2 IOIOI
# P3 IOIOIOI
# PN IOIOI...OI (O가 N개)
# I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
n = int(input().rstrip())
m = int(input().rstrip())
s = input().rstrip()

a = 0
cnt = 0
i = 1

while i < m-1:
    if s[i-1] == 'I' and s[i] == 'O' and s[i+1] == 'I':
        cnt += 1
        if cnt == n:
            cnt -= 1
            a += 1
        i += 1
    else:
        cnt = 0
    i += 1
print(a)


# =============실패__ 너무 간단하게 생각함
import sys
input = sys.stdin.readline

n = int(input().rstrip())
s_l = int(input().rstrip())
n_s = 'I' + 'OI' * n
s = input().rstrip()

print(len(s.split(n_s)))
