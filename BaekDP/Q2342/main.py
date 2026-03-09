import sys

input = sys.stdin.readline

INF = 1000000
command = list(map(int, input().split()))
max_val = INF
dp = [[max_val] * 5 for _ in range(5)]

left, right = 0, 0

def move_cost(point, step):
    if point == 0:
        return 2
    d = abs(point - step)
    if d == 0: return 1
    if d == 2: return 4
    if d == 1 or d == 3: return 3

dp[0][0] = 0

for x in command:
    if x == 0:
        break

    new_dp = [[INF] * 5 for _ in range(5)]

    for l in range(5):
        for r in range(5):
            if dp[l][r] == INF:
                continue

            # 왼발로 x 밟기
            new_dp[x][r] = min(
                new_dp[x][r],
                dp[l][r] + move_cost(l, x)
            )

            # 오른발로 x 밟기
            new_dp[l][x] = min(
                new_dp[l][x],
                dp[l][r] + move_cost(r, x)
            )

    dp = new_dp

answer = INF
for l in range(5):
    for r in range(5):
        answer = min(answer, dp[l][r])
print(answer)
