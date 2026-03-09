N = int(input())

for i in range(N):
    n = int(input())
    fir, sec, thi, fou = 1, 1, 2, 4
    summary = 0
    if n < 2:
        print(fir)
    elif n == 2:
        print(thi)
    elif n == 3:
        print(fou)
    else:
        for j in range(4, n+1):
            summary = fir + sec + thi + fou
            fir = sec
            sec = thi
            thi = fou
            fou = summary
        print(summary)
