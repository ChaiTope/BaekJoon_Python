from collections import deque

dist = [-1 for _ in range(100001)]
prev = [-1 for _ in range(100001)]

N, K = map(int, input().split())
dist[N] = 0

def bfs():
    queue = deque([N])

    while queue:
        node = queue.popleft()
        if node == K:
            return dist[node], find_prev(node, [])

        new_nodes = (node-1, node+1, node*2)
        for new_node in new_nodes:
            if 0 <= new_node < 100001:
                if dist[new_node] == -1:
                    prev[new_node] = node
                    dist[new_node] = dist[node] + 1
                    queue.append(new_node)

def find_prev(node, path):
    while True:
        path.append(node)
        if node == N:
            return path
        else:
            node = prev[node]


length, res = bfs()
print(length)
print(*reversed(res))