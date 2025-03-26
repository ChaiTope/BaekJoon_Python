import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().strip().split())
note = []

for _ in range(N):
    voca = sys.stdin.readline().strip()
    if len(voca) >= M:
        note.append(voca)
    else:
        continue

counter = Counter(note)

sorted_words = sorted(counter.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for k, v in sorted_words:
    print(k)