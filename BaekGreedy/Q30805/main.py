import sys
from collections import defaultdict
import bisect

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

posA = defaultdict(list)
posB = defaultdict(list)

for i, x in enumerate(A):
    posA[x].append(i)

for i, x in enumerate(B):
    posB[x].append(i)

candidates_desc = sorted(set(posA) & set(posB), reverse=True)
ans = []

def next_pos(sorted_indices, cur):
    k = bisect.bisect_right(sorted_indices, cur)  # cur보다 큰 첫 위치
    return sorted_indices[k] if k < len(sorted_indices) else None

ia, ib = -1, -1
for v in candidates_desc:  # 큰 값부터
    while True:
        iA = next_pos(posA[v], ia)
        iB = next_pos(posB[v], ib)
        if iA is None or iB is None:
            break
        ans.append(v)
        ia, ib = iA, iB
        # 그리고 다시 '가장 큰 값'부터 재검사

print(len(ans))
print(*ans)