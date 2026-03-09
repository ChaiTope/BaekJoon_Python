import sys

input = sys.stdin.readline

N, M, H = map(int, input().split())

vals = [list(map(int, input().split())) for _ in range(M)]
ladders = [[False] * (N+1) for _ in range(H+1)]
ans = float('inf')

for i, j in vals:
    ladders[i][j] = True

def check():
    for i in range(1, N+1):
        pos = i

        for row in range(1, H+1):
            if ladders[row][pos]:
                pos += 1
            elif ladders[row][pos - 1]:
                pos -= 1

        if pos != i:
            return False

    return True

def dfs(idx, added, limit):
    global ans

    if check() == True:
        ans = min(ans, added)
        return

    if added == limit:
        return

    for x in range(idx, H*(N-1)):
        row = x // (N-1) + 1
        col = x % (N-1) + 1

        if can_place(row, col):
            ladders[row][col] = True
            dfs(x + 1, added + 1, limit)
            ladders[row][col] = False

def can_place(row, col):
    if ladders[row][col]:
        return False

    if col > 1 and ladders[row][col - 1]:
        return False

    if col < N - 1 and ladders[row][col + 1]:
        return False

    return True

if check():
    print(0)
    sys.exit(0)

for i in range(4):
    dfs(0, 0, i)
    if ans != float('inf'):
        print(ans)
        sys.exit(0)

print(-1)