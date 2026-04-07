N = int(input())
weight = {}
R = 9

for _ in range(N):
    L = input().strip()
    n = len(L)
    for j in range(n):
        if L[j] not in weight:
            weight[L[j]] = 0
        weight[L[j]] += 10 ** (n - j - 1)

res = 0
weight = sorted(weight.items(), key=lambda x: x[1], reverse=True)

for i in range(len(weight)):
    res += weight[i][1] * R
    R -= 1

print(res)