# Bronze 4_5893
# 이진수 N이 입력으로 들어오면 17을 곱한 다음 이진수로 출력하는 프로그램을 작성하시오.

a = input()
b = int(a, 2) * 17
c = str(bin(b))
print(c[2:])