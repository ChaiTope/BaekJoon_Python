array = input()
count = 0
ans = 0

for i in range(len(array)):
    if array[i] == '(':
        count += 1

    else:
        count -= 1

        if array[i-1] == '(':
            ans += count
        else:
            ans += 1
print(ans)