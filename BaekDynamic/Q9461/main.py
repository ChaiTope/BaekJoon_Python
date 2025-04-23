T = int(input())
val = [0] * 101  # num은 최대 100까지 주어짐

# 초기값 설정
val[0] = val[1] = val[2] = 1

for i in range(3, 101):
    val[i] = val[i - 2] + val[i - 3]

for _ in range(T):
    n = int(input())
    print(val[n - 1])  # 문제는 1-indexed임 (P(1) = 1)
