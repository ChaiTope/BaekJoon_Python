N = int(input())

A = N // 10
B = N % 10
cnt = 0

while True:
    C = (A + B) % 10
    new = B * 10 + C
    cnt += 1

    if new == N:
        break

    A = B
    B = C

print(cnt)