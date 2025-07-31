import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(N)]

used = [False]*26  # 알파벳 a~z 체크
count = 0

def dfs(i, j, cnt):
    idx = ord(arr[i][j]) - ord('A')
    if used[idx]:
        return
    used[idx] = True

    global count
    count = max(count, cnt)

    for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < M:
            dfs(ni, nj, cnt+1)

    used[idx] = False

dfs(0, 0, 1)

print(count)