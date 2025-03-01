N = int(input())

pnt = []

for i in range(N):
    x, y = map(int, input().split())
    pnt.append((y, x))

pnt.sort()

for x, y in pnt:
    print(y, x)