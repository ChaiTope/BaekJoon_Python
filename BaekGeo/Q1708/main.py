import sys
import math

input = sys.stdin.readline

N = int(input())
points = []

for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

# 혹시 중복 점이 있을 수 있으니 한 번 제거
points = list(set(points))
N = len(points)

# 1. 기준점(pivot): y가 가장 작고, 같으면 x가 가장 작은 점
pivot = min(points, key=lambda p: (p[1], p[0]))
px, py = pivot

# 2. pivot 기준으로 각도 + 거리 순 정렬
def polar_key(p):
    if p == pivot:
        return (-math.pi, 0)   # pivot은 맨 앞으로 오게
    angle = math.atan2(p[1] - py, p[0] - px)
    dist2 = (p[0] - px) ** 2 + (p[1] - py) ** 2
    return (angle, dist2)

points.sort(key=polar_key)

# 3. ccw 함수: 세 점의 방향 (양수=반시계, 0=일직선, 음수=시계)
def ccw(a, b, c):
    ax, ay = a
    bx, by = b
    cx, cy = c
    return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)

# 4. 그레이엄 스캔으로 볼록껍질 만들기
stack = []

for p in points:
    # 스택에 최소 2개 이상 있을 때, 오른쪽으로 꺾이거나 일직선이면 pop
    while len(stack) >= 2 and ccw(stack[-2], stack[-1], p) <= 0:
        stack.pop()
    stack.append(p)

print(len(stack))
