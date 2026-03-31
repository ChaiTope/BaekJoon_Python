N = int(input())
A = list(map(int, input().split()))
ans = 0
visited = [False] * N
def dfs(D, L, T):
    global ans
    if D == N:
        ans = max(ans, T)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            if D == 0:
                dfs(D + 1, A[i], 0)
            else:
                dfs(D + 1, A[i], T + abs(L -  A[i]))
            visited[i] = False

dfs(0, 0, 0)
print(ans)