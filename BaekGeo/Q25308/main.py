import sys, math
from itertools import permutations

input = sys.stdin.readline

def is_convex(perm):
    # perm[k] 을 θ=k·45° 위치의 반지름으로 쓰고 좌표로 변환
    pts = []
    for k, r in enumerate(perm):
        theta = math.pi/4 * k
        pts.append((r*math.cos(theta), r*math.sin(theta)))

    # CCW로 꺾임 방향이 모두 같아야 볼록
    prev = 0
    for i in range(8):
        x1,y1 = pts[i]
        x2,y2 = pts[(i+1)%8]
        x3,y3 = pts[(i+2)%8]
        cross = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)
        if cross != 0:
            curr = 1 if cross>0 else -1
            if prev and curr != prev:
                return False
            prev = curr
    return True

radii = list(map(int, input().split()))
ans = 0

for perm in permutations(radii):
    if is_convex(perm):
        ans += 1

print(ans)
