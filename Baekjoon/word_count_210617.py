# Bronze 2_1152
# 영어 대소문자와 띄어쓰기만으로 이루어진 문자열이 주어진다.
# 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오.
# 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

string = input("")
words = string.split(" ")
words = [w for w in words if w != ""] # 공백이 아닌 경우에만 words에 넣음 # 리스트 조건제시법
print(len(words))

# 다른 방법

from sys import stdin

word = stdin.readline()
if word == ' ':
    print(0)
else:
    word = word.lstrip()
    word = word.rstrip()
    word = word.split(' ')
print(len(word))