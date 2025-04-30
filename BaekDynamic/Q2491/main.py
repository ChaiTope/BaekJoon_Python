N = int(input())
arr = list(map(int, input().split()))

inc = dec = 1
ans = 1

for i in range(1, N):
    if arr[i] == arr[i-1]:
        inc, dec = inc+1, dec+1
    else:
        if arr[i] > arr[i-1]:
            inc += 1
        else:
            inc = 1

        if arr[i] < arr[i-1]:
            dec += 1
        else:
            dec = 1

    ans = max(ans, inc, dec)

print(ans)
