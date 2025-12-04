import sys
import heapq

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
d = int(input())

ava = []

for h, o in arr:
    start, end = min(h, o), max(h, o)

    if end - start > d:
        continue

    ava.append((start, end))

ava = sorted(ava, key=lambda x: x[1])
min_heap = []
ans = 0

for start, end in ava:
    # 일단 이 구간을 현재 철로 후보에 포함시켜본다
    heapq.heappush(min_heap, start)

    # 철로 구간은 [end - d, end]
    # 이 구간보다 왼쪽에 있는(start < end - d) 애들은 더 이상 못 태우니까 빼야 함
    while min_heap and min_heap[0] < end - d:
        heapq.heappop(min_heap)

    # 지금 힙에 남아 있는 애들 = 현재 end 기준으로 철로에 완전히 들어오는 사람 수
    ans = max(ans, len(min_heap))

print(ans)