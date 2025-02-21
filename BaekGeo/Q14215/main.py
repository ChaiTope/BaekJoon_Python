tri = sorted(map(int, input().split()))
if tri[0] + tri[1] <= tri[2]:
    print(2*(tri[0] + tri[1])-1)
else:
    print(tri[0] + tri[1] + tri[2])