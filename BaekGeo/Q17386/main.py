import sys

x1, y1, x2, y2 = map(int, input().split())

x3, y3, x4, y4 = map(int, input().split())

def ccw(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

ccw1 = ccw((x1,y1), (x2,y2), (x3,y3))
ccw2 = ccw((x1,y1), (x2,y2), (x4,y4))
ccw3 = ccw((x3,y3), (x4,y4), (x1,y1))
ccw4 = ccw((x3,y3), (x4,y4), (x2,y2))

# x축 범위 겹침?
if max(min(x1, x2), min(x3, x4)) <= min(max(x1, x2), max(x3, x4)):
    # y축 범위 겹침?
    if max(min(y1, y2), min(y3, y4)) <= min(max(y1, y2), max(y3, y4)):
        if ccw1 * ccw2 <= 0:
            if ccw3 * ccw4 <= 0:
                print(1)
                sys.exit(0)

print(0)