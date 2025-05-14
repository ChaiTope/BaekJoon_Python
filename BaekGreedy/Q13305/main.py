import sys

input = sys.stdin.readline

N = int(input())

way = list(map(int, input().split()))

price = list(map(int, input().split()))
price.pop()
total = 0
min_val = float('inf')

for i in range(N-1):
    min_val = min(min_val, price[i])

    total += min_val * way[i]

print(total)