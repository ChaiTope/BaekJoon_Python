import sys

N = int(input())
inp = list(map(int, sys.stdin.readline().strip().split()))

out = sorted(inp)
count = 0
res = [[] for _ in range(N)]
for i in range(N-1):
    if out[i] != out[i+1]:
        res[i] = count
        count += 1
    else:
        res[i] = count
if out[N-1] == out[N-2]:
    res[N-1] = count
else:
    res[N-1] = count+1

sol = []

for i in range(N):
    for j in range(N):
        if inp[i] == out[j]:
            sol.append(res[j])
            break

sys.stdout.write(" ".join(map(str, sol)))
