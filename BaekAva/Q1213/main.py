N = int(input())

a = ("* " * ((N + 1) // 2)).rstrip()
b = (" *" * (N // 2)).rstrip()

for _ in range(N):
    print(a)
    print(b)