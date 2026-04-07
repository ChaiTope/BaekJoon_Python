R = 0
for i in range(int(input())):
    S = []
    for a in input():
        if S and S[-1] == a:
            S.pop()
            continue
        S.append(a)
    if not S:
        R += 1
print(R)