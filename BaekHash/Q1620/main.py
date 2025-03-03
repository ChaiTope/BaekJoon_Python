import sys

N, M = map(int, input().split())
poke_num = {}
poke_name = {}

for i in range(1, N + 1):
    name = sys.stdin.readline().strip()
    poke_num[i] = name
    poke_name[name] = i

res = []

for _ in range(M):
    exp = sys.stdin.readline().strip()
    if exp.isdigit():
        res.append(poke_num[int(exp)])
    else:
        res.append(str(poke_name[exp]))

print("\n".join(res))