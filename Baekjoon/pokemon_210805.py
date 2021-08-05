# Silver 4_1620

# 첫째 줄에는 도감에 수록되어 있는 포켓몬의 개수 N이랑 내가 맞춰야 하는 문제의 개수 M이 주어져.
# N과 M은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수이고,
# 둘째 줄부터 N개의 줄에 포켓몬의 번호가 1번인 포켓몬부터 N번에 해당하는 포켓몬까지 한 줄에 하나씩 입력으로 들어와.
# 포켓몬의 이름은 모두 영어로만 이루어져있고, 또, 음... 첫 글자만 대문자이고, 나머지 문자는 소문자로만 이루어져 있어.
# 포켓몬 이름의 최대 길이는 20이야.
# 그 다음 줄부터 총 M개의 줄에 내가 맞춰야하는 문제가 입력으로 들어와.
# 문제가 알파벳으로만 들어오면 포켓몬 번호를 말해야 하고, 숫자로만 들어오면, 포켓몬 번호에 해당하는 문자를 출력해야해.
# 입력으로 들어오는 숫자는 반드시 1보다 크거나 같고, N보다 작거나 같고,
# 입력으로 들어오는 문자는 반드시 도감에 있는 포켓몬의 이름만 주어져.

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
number_pokemon = 1
pokemon_dict1 = {}
pokemon_dict2 = {}

for _ in range(N):
    name = str(input()).strip()
    pokemon_dict1[number_pokemon] = name
    pokemon_dict2[name] = number_pokemon
    number_pokemon += 1

answer = []
for _ in range(M):
    pokemon = str(input()).strip()
    try:
        print(pokemon_dict1[int(pokemon)])
    except:
        print(pokemon_dict2[pokemon])


# =====런타임 에러
n, m = map(int, input().split())
poke_dic = []

for i in range(n):
    poke_name = input()
    poke_dic.append(poke_name)

for j in range(m):
    q = input()
    if q.isdigit():
        print(poke_dic[int(q)+1])
    else:
        print(poke_dic.index(q)+1)