import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(map(int, input().split()))

visited = [False]*N
path = []

def backtrack():
    if len(path) == M:
        print(*path)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            path.append(nums[i])

            backtrack()

            path.pop()
            visited[i] = False

backtrack()
