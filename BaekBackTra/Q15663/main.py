N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
used = [False] * N
path = []
result = []

def backtrack():
    if len(path) == M:
        result.append(tuple(path))  # 중복 제거용
        return

    prev = -1  # 같은 depth에서 중복 수 체크
    for i in range(N):
        if not used[i] and arr[i] != prev:
            used[i] = True
            path.append(arr[i])
            backtrack()
            path.pop()
            used[i] = False
            prev = arr[i]  # 이걸 갱신함으로써 같은 depth 내 중복 제거

backtrack()

# 중복 제거 후 정렬해서 출력
for seq in sorted(set(result)):
    print(' '.join(map(str, seq)))
