import sys

input = sys.stdin.readline

N = int(input())

array = list(map(int, input().split()))

T, P = map(int, input().split())
result = 0
for i in array:
    if i % T == 0:
        result += i // T
    else:
        result += i // T + 1

print(result)
print(N//P, N%P)