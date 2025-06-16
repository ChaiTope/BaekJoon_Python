import sys
input = sys.stdin.readline

def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def on_segment(a, b, p):
    return (min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and
            min(a[1], b[1]) <= p[1] <= max(a[1], b[1]))

def segments_intersect(A, B, C, D):
    # Bounding box check
    if (max(min(A[0], B[0]), min(C[0], D[0])) > min(max(A[0], B[0]), max(C[0], D[0]))) or \
       (max(min(A[1], B[1]), min(C[1], D[1])) > min(max(A[1], B[1]), max(C[1], D[1]))):
        return False
    # CCW check
    ccw1 = ccw(A, B, C)
    ccw2 = ccw(A, B, D)
    ccw3 = ccw(C, D, A)
    ccw4 = ccw(C, D, B)
    if ccw1 * ccw2 < 0 and ccw3 * ccw4 < 0:
        return True
    # Collinear overlap
    if ccw1 == 0 and on_segment(A, B, C): return True
    if ccw2 == 0 and on_segment(A, B, D): return True
    if ccw3 == 0 and on_segment(C, D, A): return True
    if ccw4 == 0 and on_segment(C, D, B): return True
    return False

def intersection_point(A, B, C, D):
    # Returns (delta_x, delta_y, delta) or None
    x1, y1 = A; x2, y2 = B
    x3, y3 = C; x4, y4 = D
    delta = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if delta == 0:
        return None
    delta_x = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
    delta_y = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
    return delta_x, delta_y, delta

# Read input as integers
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
A, B = (x1, y1), (x2, y2)
C, D = (x3, y3), (x4, y4)

if segments_intersect(A, B, C, D):
    res = intersection_point(A, B, C, D)
    if res is not None:
        dx, dy, delta = res
        x = dx / delta
        y = dy / delta
        eps = 1e-9
        # Check if nearly integer
        if abs(x - round(x)) < eps and abs(y - round(y)) < eps:
            xi, yi = round(x), round(y)
            print(1)
            print(xi, yi)
        else:
            print(1)
            print(f"{x:.9f} {y:.9f}")
    else:
        # Collinear case: collect common points
        ccw1 = ccw(A, B, C)
        ccw2 = ccw(A, B, D)
        ccw3 = ccw(C, D, A)
        ccw4 = ccw(C, D, B)
        candidates = []
        if ccw1 == 0 and on_segment(A, B, C): candidates.append(C)
        if ccw2 == 0 and on_segment(A, B, D): candidates.append(D)
        if ccw3 == 0 and on_segment(C, D, A): candidates.append(A)
        if ccw4 == 0 and on_segment(C, D, B): candidates.append(B)
        uniq = list({(p[0], p[1]) for p in candidates})
        if len(uniq) == 1:
            x, y = uniq[0]
            print(1)
            print(x, y)
        else:
            print(1)
else:
    print(0)

