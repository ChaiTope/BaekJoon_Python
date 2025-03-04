from collections import Counter

N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dup = []
for i in a:
    dup.append(i)
for i in b:
    dup.append(i)

dup = Counter(dup)
count = 0
for i in dup:
    if dup[i] > 1:
        count += 1

print(len(a) + len(b) - count * 2)
