from collections import Counter

N = int(input())
sang = map(int, input().split())
M = int(input())
Me = map(int, input().split())

s_count = Counter(sang)

for m in Me:
    print(s_count.get(m, 0), end=' ')