import sys

input = sys.stdin.readline

V = int(input())
tree = [0 for _ in range(V + 1)]

for i in range(V):
    nodes = list(map(int, input().split()))
    node = nodes[0]

    for j in range(1, len(nodes), 2):
        if nodes[j] == -1:
            break

        tree[node].append()
