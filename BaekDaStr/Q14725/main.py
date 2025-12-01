import sys

input = sys.stdin.readline

N = int(input())

tree = {}

for i in range(N):
    cur = tree

    root = input().split()
    for j in root[1:]:
        if j not in cur:
            cur[j] = {}

        cur = cur[j]

def dfs(node, depth):
    for key in sorted(node.keys()):
        print("--"*depth + key)
        dfs(node[key], depth+1)

dfs(tree, 0)