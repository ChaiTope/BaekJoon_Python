from math import sqrt
from math import floor

N = int(input())

for i in range(N):
    M = int(input())
    x = floor(sqrt(M))
    b = True
    while b:
        for j in range(2, x):
            if x % j == 0:
                break
            elif x == j:
                print(M)
                b = False
                break
            else:
                M = M + 1
                break
