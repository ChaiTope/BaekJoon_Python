from collections import deque

T = int(input())

for i in range(T):
    array = deque(list(map(int, input().split())))
    N = array.popleft()
    avg = sum(array) / N

    cnt = 0

    for x in array:
        if x > avg:
            cnt += 1

    res = 100 / len(array) * cnt

    print(f"{res:.3f}" + "%")