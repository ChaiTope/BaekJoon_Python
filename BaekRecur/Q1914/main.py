import sys

N = int(input())
result = []

def hanoi(n, start, to, via):
    if n == 1:
        result.append((start, to))
    else:
        hanoi(n - 1, start, via, to)
        result.append((start, to))
        hanoi(n - 1, via, to, start)

def hanonoi(n):
    return (2 ** n) - 1

if N <= 20:
    hanoi(N, 1, 3, 2)
    print(len(result))
    for a, b in result:
        sys.stdout.write(f"{a} {b}\n")
else:
    print(hanonoi(N))