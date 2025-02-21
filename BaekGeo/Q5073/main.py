res = []
while True:
    a = list(map(int, input().split()))
    a = sorted(a)
    if a[0] == 0 and a[1] == 0 and a[2] == 0:
        break
    elif a[0] == a[1] == a[2]:
        res.append("Equilateral")
    elif a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
        if a[0] + a[1] > a[2]:
            res.append("Isosceles")
        else:
            res.append("Invalid")
    else:
        if a[0] + a[1] > a[2]:
            res.append("Scalene")
        else:
            res.append("Invalid")

print("\n".join(res))