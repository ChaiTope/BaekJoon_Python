x1, y1, a1, x2, y2, a2 = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (x1 * x + y1 * y == a1) and (x2 * x + y2 * y == a2):
            print(x, y)
            exit()