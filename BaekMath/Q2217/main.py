N = int(input())
lopes = sorted([int(input()) for _ in range(N)], reverse=True)
wh = 0
for i in range(N, 0, -1):
    wh = max(wh, lopes[i-1]*i)
print(wh)