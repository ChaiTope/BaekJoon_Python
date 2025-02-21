bead = [list(map(int, input().split())) for _ in range(int(input()))]
x, y = zip(*bead)
print((max(x)-min(x)) * (max(y)-min(y)))