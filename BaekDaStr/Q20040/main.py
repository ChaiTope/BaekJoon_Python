import sys

input = sys.stdin.readline

n, m = map(int, input().split())

parent = [0] * n
ans = 0

for i in range(n):
    parent[i] = i

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # 경로 압축 (한 단계씩 건너뛰기)
        x = parent[x]
    return x


def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra == rb: return False
    parent[rb] = ra
    return True

for i in range(1, m+1):
    a, b = map(int, input().split())
    if not union(a, b):
        ans = i
        break

print(ans)