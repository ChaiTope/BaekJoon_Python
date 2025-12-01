import sys

input = sys.stdin.readline

N = int(input())
nodes = [[] for _ in range(N + 1)]
dp = [[0] * 2 for _ in range(N + 1)]

parent = [0] * (N+1)
order = []

stack = [1]
parent[1] = -1   # 루트의 부모는 없음 표시

for i in range(N - 1):
    a, b = map(int, input().split())

    nodes[a].append(b)
    nodes[b].append(a)

while stack:
    u = stack.pop()
    order.append(u)

    for v in nodes[u]:
        if v == parent[u]:
            continue
        parent[v] = u
        stack.append(v)

for u in reversed(order):
    dp[u][0] = 0      # u 일반인
    dp[u][1] = 1      # u 얼리 아답터 (본인)

    for v in nodes[u]:
        if v == parent[u]:
            continue

        dp[u][0] += dp[v][1]
        dp[u][1] += min(dp[v][0], dp[v][1])

print(min(dp[1][0], dp[1][1]))
