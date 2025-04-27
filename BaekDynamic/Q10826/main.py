fi = [0] * 3

fi[0] = 0
fi[1] = 1

N = int(input())
if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    for i in range(2, N+1):
        fi[2] = fi[0] + fi[1]
        fi[0] = fi[1]
        fi[1] = fi[2]

    print(fi[2])