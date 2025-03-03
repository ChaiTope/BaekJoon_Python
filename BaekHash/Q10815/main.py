N = int(input())
sang = set(map(int, input().split()))
M = int(input())
Me = list(map(int, input().split()))

for i in Me:
    if i in sang:
        print(1, end=" ")
    else:
        print(0, end=" ")