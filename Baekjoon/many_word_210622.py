# Bronze 2_1371
# 영어에서는 어떤 글자가 다른 글자보다 많이 쓰인다. 예를 들어, 긴 글에서 약 12.31% 글자는 e이다.
# 어떤 글이 주어졌을 때, 가장 많이 나온 글자를 출력하는 프로그램을 작성하시오.

import sys

s = sys.stdin.read()
li = [0]*26
for c in s:
    if c.islower():
        li[ord(c)-97] += 1
for i in range(26):
    if li[i] == max(li):
        print(chr(97+i), end='')


# Counter 사용
from collections import Counter
from sys import stdin

input = stdin.readline
a = input()
b = Counter(a)  # 각 문자 갯수 확인
c = 0  # 문자 개수 넣을 변수
d = ''  # 가장 많은 문자
for i, j in b.items():
    if i == ' ' or i == '\n' or i ==',' or i =='.' :  # 문자가 아닌거 제외
        continue
    if b[i] > c:  # 현재 문자의 개수와 c와 비교
        c = b[i]
        d = i
    elif b[i] == c:  # 같으면 d에 포함
        d += i

dd = []  # d를 알파벳 순으로 아스키 코드로 변환
for i in d:
    dd.append(ord(i))
dd.sort()

cc = ''
for i in dd:  # 다시 문자로
    cc += chr(i)

print(cc)