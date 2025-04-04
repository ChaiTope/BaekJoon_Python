def solve(row):
    global count
    if row == N:
        count += 1
        return

    for col in range(N):
        if col in cols or (row + col) in diag1 or (row - col) in diag2:
            continue

        cols.add(col)
        diag1.add(row + col)
        diag2.add(row - col)

        solve(row + 1)

        cols.remove(col)
        diag1.remove(row + col)
        diag2.remove(row - col)

N = int(input())
count = 0
cols = set()
diag1 = set()
diag2 = set()

solve(0)
print(count)