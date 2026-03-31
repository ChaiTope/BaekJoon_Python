import sys

input = sys.stdin.readline

N = int(input())

nodes = list(map(int, input().split()))
tree = [[] for _ in range(N)]
e = int(input())
root = -1

for i in range(N):
    if nodes[i] == -1:
        root = i
        if i == e:
            print(0)
            sys.exit(0)
        continue
    tree[nodes[i]].append(i)

parent = nodes[e]

if parent != -1:
    tree[parent].remove(e)

cnt = 0

def dfs(x):
    global cnt

    if tree[x] == []:
        cnt += 1
        return

    for child in tree[x]:
        dfs(child)

dfs(root)
print(cnt)