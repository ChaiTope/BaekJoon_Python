a = []
for _ in range(3):
    a.append(int(input()))
if a[0]+a[1]+a[2] == 180:
    if a[0] == a[1] == a[2]:
        print("Equilateral")
    elif a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")


a = [int(input()) for _ in range(3)]
if sum(a) == 180:
    print(["Equilateral", "Isosceles", "Scalene"][len(set(a))-1])
else:
    print("Error")