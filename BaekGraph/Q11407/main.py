import sys
from collections import deque

input = sys.stdin.readline
N = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(N)]

# 결과 행렬 초기화
result = [[0] * N for _ in range(N)]

# 각 정점 i에서 BFS로 도달 가능한 정점 탐색
for i in range(N):
    visited = [False] * N
    queue = deque()

    # i에서 직접 연결된 이웃들을 큐에 추가
    for j in range(N):
        if graph[i][j] == 1:
            visited[j] = True
            queue.append(j)

    # BFS
    while queue:
        cur = queue.popleft()
        for nxt in range(N):
            if graph[cur][nxt] == 1 and not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

    # 방문된 정점들을 결과 행렬에 기록
    for j in range(N):
        if visited[j]:
            result[i][j] = 1

# 출력
out = []
for row in result:
    out.append(' '.join(map(str, row)))
print("\n".join(out))
