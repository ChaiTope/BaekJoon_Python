N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

partner = []

def backtrack(start, path):
    if len(path) == N // 2:
        partner.append(path[:])  # 복사본 추가
        return

    for i in range(start, N):
        path.append(i)
        backtrack(i + 1, path)
        path.pop()

def synergy(array):
    total = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            total += arr[array[i]][array[j]] + arr[array[j]][array[i]]
    return total

def maker(array):
    min_val = float('inf')
    length = len(array)
    for i in range(length // 2):
        team1 = array[i]
        team2 = array[length - 1 - i]
        diff = abs(synergy(team1) - synergy(team2))
        min_val = min(min_val, diff)
    return min_val

backtrack(0, [])
print(maker(partner))
