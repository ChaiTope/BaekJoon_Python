N, M = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))

path = []
result = []

def backtrack():
    if len(path) == M:
        result.append(tuple(path))  # 중복 제거용
        return

    for i in range(len(arr)):
        if len(path) == 0:
            path.append(arr[i])
            backtrack()
            path.pop()
        elif arr[i] >= path[-1]:
            path.append(arr[i])
            backtrack()
            path.pop()

backtrack()

# 중복 제거 후 정렬해서 출력
for seq in sorted(set(result)):
    print(' '.join(map(str, seq)))
