# Bronze 5_15727

# 성우는 1분에 1에서 5까지의 거리를 이동할 수 있다.
# 성우가 있는 곳으로부터 민건이의 집까지 거리가 주어졌을 때,
# 최대한 빨리 찾을 경우, 정확히 몇 분만에 민건이를 찾을 수 있는지 출력하는 프로그램을 작성하시오.
# 첫째 줄에 성우의 현재 위치와 민건이의 집까지의 거리 L(1 ≤ L ≤ 1,000,000)가 주어진다.

lengh = int(input())
lengh -= 1
print(lengh//5+1)

# 입력으로 조장의 집까지의 거리가 주어지고 1분에 1~5까지의 거리를 간다
# 거리가 1이여도 1분이 걸리고, 거리가 5여도 1분이 걸린다.
# 따라서 거리가 들어왔을 때 거리/5 의 몫에 +1를 해주어야한다.
# 여기서 한가지 오류는 만약 a가 5 이하 이거나 5의 배수 일 때 오류가 1분 차이가 난다
# L = 5 일때 실제 걸리는 시간은 1분이지만 위 식으로는 5//5 +1 =2 가 된다.
# 따라서 이 오류를 방지해주기 위해서 들어온 거리 -1 을 한 거리를 계산에 사용한다.
