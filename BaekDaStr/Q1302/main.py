from collections import Counter

N = int(input())
A = []
for i in range(N):
    A.append(input())
print(min(Counter(A).items(), key=lambda x: (-x[1], x[0]))[0])