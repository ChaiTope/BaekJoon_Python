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

hanoi(N, 1, 3, 2)

print(len(result))
for a, b in result:
    sys.stdout.write(f"{a} {b}\n")
