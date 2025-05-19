import collections
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

start = collections.deque()

start.append(N)

dist = [-1] * 100001

dist[N] = 0
def bfs(start, end):
    while start:
        x = start.popleft()    # 가장 먼저 넣은 위치 꺼내고
        if x == end:
            print(dist[x])     # 목표에 도달한 순간 최소 시간이니까 출력 후 종료
            return
        for nx in (x-1, x+1, x*2):
            # 범위 체크
            if 0 <= nx <= 100000 and dist[nx] == -1:
                dist[nx] = dist[x] + 1   # 한 칸(혹은 순간이동)만큼 시간 추가
                start.append(nx)        # 다음에 탐색할 위치로 큐에 추가
bfs(start, K)
