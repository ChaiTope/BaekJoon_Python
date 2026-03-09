import sys
import math
A, B, C = map(int, input().split())
T = 1

if B >= C:
    print(-1)
    sys.exit(0)

T = math.floor(A / (C-B)) + 1

print(T)