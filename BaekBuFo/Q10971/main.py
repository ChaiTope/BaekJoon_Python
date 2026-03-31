N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
answer = float('inf')

def dfs(start, i, visit, cost):
    global answer

    if visit == N:
        if A[i][start] != 0:
            answer = min(answer, cost + A[i][start])
        return

    if cost >= answer:
        return

    for j in range(N):
        if not visited[j] and A[i][j] != 0:
            visited[j] = True
            dfs(start, j, visit + 1, cost + A[i][j])
            visited[j] = False

visited[0] = True
dfs(0, 0, 1, 0)

print(answer)