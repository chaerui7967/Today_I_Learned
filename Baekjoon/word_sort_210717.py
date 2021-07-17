# Silver 5_1181

# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
#
# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로

n = int(input())
words = []

for _ in range(n):
    word = str(input())
    word_count = len(word)
    words.append((word, word_count))

#중복 삭제
words = list(set(words))

#단어 숫자 정렬 > 단어 알파벳 정렬
words.sort(key = lambda word: (word[1], word[0]))

for word in words:
    print(word[0])