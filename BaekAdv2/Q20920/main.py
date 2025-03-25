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

most_common = counter.most_common()

for k, v in most_common:
    print(k)