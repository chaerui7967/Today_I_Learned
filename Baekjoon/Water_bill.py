# Bronze 4_10707
# X사 : 1리터당 A엔.
# Y사 : 기본요금은 B엔이고, 사용량이 C리터 이하라면 요금은 기본요금만 청구된다.
# 사용량이 C리터가 넘었을 경우 기본요금 B엔에 더해서 추가요금이 붙는다.
# 추가요금은 사용량이 C리터를 넘었을 경우 1리터를 넘었을 때마다 D엔이다.
# 집에서 한 달간 쓰는 수도의 양은 P리터이다.
# 수도요금이 최대한 싸게 되도록 수도회사를 고를 때, 집의 1달간 수도요금을 구하여라.

a = int(input())
b = int(input())
c = int(input())
d = int(input())
P = int(input())
fee = 0
if P > c :
    fee = (P-c) * d + b
    if a*P < fee:
        fee = a*P
else:
    if b > a*P:
        fee = a*P
    else:
        fee = b
print(fee)