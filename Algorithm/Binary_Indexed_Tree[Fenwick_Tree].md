## 펜윅 트리 (바이너리 인덱스 트리)

Fenwick Tree는 Binary Indexed Tree라고도 하며, 줄여서 BIT라고 합니다.

Fenwick Tree를 구현하려면, 어떤 수 X를 이진수로 나타냈을 떄, 마지막 1의 위치를 알아야 합니다.

- 3 = 1**1**2
- 5 = 10**1**2
- 6 = 1**1**02
- 8 = **1**0002
- 9 = 100**1**2
- 10 = 10**1**02
- 11 = 101**1**2
- 12 = 1**1**002
- 16 = **1**00002

마지막 1이 나타내는 값을 `L[i]`라고 표현하겠습니다. `L[3] = 1`, `L[10] = 2`, `L[12] = 4`이 됩니다.

수 N개를 `A[1]` ~ `A[N]`이라고 했을 때, `Tree[i]`는 `A[i]` 부터 앞으로 `L[i]`개의 합이 저장되어 있습니다.

아래 그림은 각각의 `i`에 대해서, `L[i]`를 나타낸 표입니다. 아래 초록 네모는 `i`부터 앞으로 `L[i]`개가 나타내는 구간입니다.

![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/blog/bit1.png)

`L[i] = i & -i`가 됩니다. 그 이유는 아래와 같습니다.

```
      -num = ~num + 1
       num = 100110101110101100000000000
      ~num = 011001010001010011111111111
      -num = 011001010001010100000000000
num & -num = 000000000000000100000000000
```

`A` = [3, 2, 5, 7, 10, 3, 2, 7, 8, 2, 1, 9, 5, 10, 7, 4]인 경우에, 각각의 `Tree[i]`가 저장하고 있는 값은 다음과 같게 됩니다.

![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/blog/bit2.png)

예를 들어, `Tree[12]`에는 12부터 앞으로 `L[12] = 4`개의 합은 `A[9] + A[10] + A[11] + A[12]`가 저장되어 있습니다. `Tree[7]`에는 7부터 앞으로 `L[7] = 1`개의 합인 `A[7]`이 저장되어 있습니다.

### 합 구하기

`Tree`를 이용해서 `A[1] + ... + A[13]`은 어떻게 구할 수 있을까요?

13을 이진수로 나타내면 1101입니다. 따라서, `A[1] + ... + A[13] = Tree[1101] + Tree[1100] + Tree[1000]`이 됩니다. `Tree`의 인덱스는 이진수입니다.

![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/blog/bit3.png)

`1101` -> `1100` -> `1000`는 마지막 1의 위치를 빼면서 찾을 수 있습니다. 이것을 코드로 작성해보면 다음과 같습니다.

```
int sum(int i) {
    int ans = 0;
    while (i > 0) {
        ans += tree[i];
        i -= (i & -i);
    }
    return ans;
}
```

모든 `i`에 대해서, `A[1] + ... + A[i]`를 구하는 과정을 그림으로 나타내면 다음과 같습니다.

![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/blog/bit4.png)

어떤 구간의 합 `A[i] + ... + A[j]`는 `A[1] + ... + A[j]`에서 `A[1] + ... + A[i-1]`을 뺀 값과 같습니다. 따라서, `sum(j) - sum(i-1)`을 이용해서 구할 수 있습니다.

### 변경

어떤 수를 변경한 경우에는, 그 수를 담당하고 있는 구간을 모두 업데이트해줘야 합니다. 아래와 같이 마지막 1의 값을 더하는 방식으로 구현할 수 있습니다.

```
void update(int i, int num) {
    while (i <= n) {
        tree[i] += num;
        i += (i & -i);
    }
}
```

아래 그림은 `i`를 변경했을 때, 바꿔줘야하는 `Tree[i]`를 나타낸 그림입니다.

![img](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/blog/bit5.png)

 출처 : https://www.acmicpc.net/blog/view/21