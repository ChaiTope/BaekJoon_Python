N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

coins = reversed(coins)
count = 0
for coin in coins:
    count += K // coin
    K %= coin
print(count)