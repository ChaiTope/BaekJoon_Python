import sys
from itertools import combinations

input = sys.stdin.readline
print = sys.stdout.write

N , M = map(int, input().split())

items = []
for i in range(1,N+1):
    items.append(i)

# M개를 고르는 조합 생성
comb = combinations(items, M)

for c in comb:
    print(f"{' '.join(map(str, c))}\n")