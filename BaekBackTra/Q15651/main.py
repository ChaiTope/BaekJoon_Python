import sys

input = sys.stdin.readline
print = sys.stdout.write

def backtrack(start, path):
    if len(path) == M:
        print(f"{' '.join(map(str, path))}\n")
        return

    for i in range(start, N + 1):
        path.append(i)
        backtrack(start, path)
        path.pop()

N, M = map(int, input().split())
backtrack(1, [])