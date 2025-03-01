import sys

N = int(input())
a = [[] for _ in range(50)]

for i in range(N):
    n = sys.stdin.readline().strip()
    if n not in a[len(n)-1]:
        a[len(n)-1].append(n)

# 각 리스트 내부를 정렬
for sublist in a:
    sublist.sort()

res = []

for i in range(len(a)):
    res.extend(a[i])

print("\n".join(res))