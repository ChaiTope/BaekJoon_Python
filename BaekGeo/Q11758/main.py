import sys

input = sys.stdin.readline

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
C = tuple(map(int, input().split()))

def ccw(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

res = ccw(A, B, C)
if res > 0:
    print(1)    # 반시계
elif res < 0:
    print(-1)   # 시계
else:
    print(0)    # 일직선
