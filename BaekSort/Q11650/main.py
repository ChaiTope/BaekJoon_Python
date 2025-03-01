N = int(input())

pnt = []

for i in range(N):
    x, y = map(int, input().split())
    pnt.append((x, y))

pnt.sort()

for x, y in pnt:
    print(x, y)