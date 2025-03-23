N = int(input())

chong = set()
chong.add("ChongChong")
for i in range(N):
    p1, p2 = map(str, input().split())
    if p1 in chong or p2 in chong:
        chong.add(p1)
        chong.add(p2)

print(len(chong))