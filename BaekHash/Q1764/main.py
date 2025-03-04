import sys
from collections import Counter

N, M = map(int, input().split())
mans = []
drops = []
for i in range(N + M):
    mans.append(sys.stdin.readline().strip())

m_count = Counter(mans)

print((N+M) - len(m_count))

for i in m_count:
    if m_count[i] > 1:
        drops.append(i)

print("\n".join(sorted(drops)))