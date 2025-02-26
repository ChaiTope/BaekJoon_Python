N, M = map(int, input().split())
cards = list(map(int, input().split()))

res = []
for i in range(N):
    for j in range(i+1, N):
        for l in range(j+1, N):
            total = cards[i] + cards[j] + cards[l]
            if total <= M:
                res.append(total)

print(max(res))
