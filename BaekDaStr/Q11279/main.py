import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    if x > 0:
        # 최대 힙을 만들기 위해 -x를 넣음
        heapq.heappush(heap, -x)
    else:
        # x == 0일 때
        if heap:
            # heappop 하면 가장 작은(-가장 작은) 값이 나오니까 부호를 뒤집어서 출력
            print(-heapq.heappop(heap))
        else:
            print(0)
