def backtrack(idx, result, add, sub, mul, div):
    global max_val, min_val

    if idx == n:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return

    if add > 0:
        backtrack(idx + 1, result + numbers[idx], add - 1, sub, mul, div)

    if sub > 0:
        backtrack(idx + 1, result - numbers[idx], add, sub - 1, mul, div)

    if mul > 0:
        backtrack(idx + 1, result * numbers[idx], add, sub, mul - 1, div)

    if div > 0:
        if result < 0:
            temp = -(-result // numbers[idx])
        else:
            temp = result // numbers[idx]
        backtrack(idx + 1, temp, add, sub, mul, div - 1)

n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_val = float('-inf')
min_val = float('inf')

backtrack(1, numbers[0], add, sub, mul, div)

print(max_val)
print(min_val)

