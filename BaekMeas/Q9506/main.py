
while True:
    N = int(input())
    res = []

    if N == -1:
        break
    for i in range(1, N):
        if N % i == 0:
            res.append(i)
    if sum(res) == N:
        print(N, "=", " + ".join(map(str, res)))
    else:
        print(N, "is NOT perfect.")


"""복습하고 다시 코드를 설계해보자"""

while True:
    N = int(input())
    if N == -1:
        break
    res = []
    total = 0

    for i in range(1, int(N**0.5) +1):
        if N % i == 0:
            res.append(i)
            total += i
            if i != 1 and i != N // i:
                res.append(N // i)
                total += N // i
    res.sort()
    if total == N:
        print(f"{N} = {' + '.join(map(str, res))}")
    else:
        print(f"{N} is NOT perfect.")