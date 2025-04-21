N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())))

path, result = [], []

def backtrack():
    if len(path) == M:
        result.append(tuple(path))
        return

    for i in range(len(arr)):
        path.append(arr[i])
        backtrack()
        path.pop()

backtrack()

for seq in sorted(set(result)):
    print(' '.join(map(str, seq)))