import sys

print = sys.stdout.write

def backtrack(path, visited):
    if len(path) == M:
        print(f"{' '.join(map(str, path))}\n")
        return

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            path.append(i)
            backtrack(path, visited)
            path.pop()
            visited[i] = False


N, M = map(int, input().split())
visited = [False] * (N + 1)
backtrack([], visited)
