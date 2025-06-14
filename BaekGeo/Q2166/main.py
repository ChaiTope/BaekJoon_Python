import sys

input = sys.stdin.readline

N = int(input())

def polygon_area(points):

    area = 0
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i+1) % n]   # 마지막엔 0번으로 순환
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

points = [list(map(float, input().split())) for _ in range(N)]
print(polygon_area(points))