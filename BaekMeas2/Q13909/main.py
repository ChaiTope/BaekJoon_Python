n = int(input())

arr = [1] * n
for i in range(n):
    j = i
    p = 1
    while j*p < n:
        if arr[j*p] == 0:
            arr[j] = 1
            j += 1
        else:
            arr[j*p] = 0
            j += 1
    p+=1
    print(*arr)