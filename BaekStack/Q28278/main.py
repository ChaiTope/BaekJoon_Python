import sys

n = int(sys.stdin.readline())  # 입력 최적화
arr = []
for _ in range(n):
    a = list(map(int, sys.stdin.readline().split()))  # 입력 최적화
    if a[0] == 1:
        arr.append(a[1])  # push
    elif a[0] == 2:
        if arr:
            print(arr.pop())  # pop()은 O(1)
        else:
            print(-1)
    elif a[0] == 3:
        print(len(arr))  # size
    elif a[0] == 4:
        print(0 if arr else 1)  # empty
    elif a[0] == 5:
        print(arr[-1] if arr else -1)  # top
