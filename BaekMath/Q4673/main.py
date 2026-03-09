visited = [False] * 10001

def d(n):
    nn = n
    for x in str(n):
        nn += int(x)
    return nn

for i in range(1, 10001):
    val = d(i)
    if val <= 10000:
        visited[val] = True

for i in range(1, 10001):
    if not visited[i]:
        print(i)