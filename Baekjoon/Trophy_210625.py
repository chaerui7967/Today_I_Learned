# Bronze 2_1668

# 높이가 큰 트로피가 높이가 작은 트로피의 왼쪽에 있다면, 높이가 작은 트로피는 큰 트로피에 가려서 보이지 않게 된다.
# 트로피는 자기의 앞에 (보는 사람의 관점에서) 자기보다 높이가 작은 트로피가 있을 때만 보이게 된다.
# 민식이는 선반을 180도 회전시켜서 트로피가 보이는 개수를 변하게 할 수도 있다.
# 선반위에 올려져 있는 트로피의 높이가 주어졌을 때,
# 왼쪽에서 봤을 때 보이는 개수와, 오른쪽에서 봤을 때 보이는 개수를 출력하는 프로그램을 작성하시오.

# 첫째 줄에 트로피의 개수 N (1 ≤ N ≤ 50)이 주어진다.
# 둘째 줄부터 N개의 줄에 왼쪽의 트로피부터 차례대로 높이가 주어진다.
# 트로피의 높이는 100보다 작거나 같은 자연수이다.

def ascending(trophies):
    now_max = trophies[0]
    count = 1
    for trophy in trophies:
        if trophy > now_max:
            count +=1
        now_max = max(now_max,trophy)
    return count

n = int(input())
trophies = []

for _ in range(n):
    trophies.append(int(input()))

print(ascending(trophies))
trophies.reverse()
print(ascending(trophies))

# Solution
# ascending 함수를 작성하는데
# now_max로 현재 최댓값과 count를 1로 초기화한다.
# trophies에 대해 각 요소 별로 현재 최댓값보다 크면 count를 늘린다.
# now_max는 현재 trophy와 now_max 중 큰 값을 저장하여 for문이 도는 동안 최댓값이 갱신되도록 한다.
# n과 trophies를 통해 input을 받고
# ascending을 적용한 값을 출력한다. 이는 왼쪽에서 보이는 트로피 개수이다.
# trophies의 순서를 뒤집고 다시 ascending을 적용한 값을 출력한다. 이는 오른쪽에서 보이는 트로피 개수이다.
