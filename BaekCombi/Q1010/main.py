import math

N = int(input())
for i in range(N):
    s, w = map(int, input().split())
    print(math.comb(w, s))