N = int(input())

sqr = [["*"] * N for _ in range(N)]

def erase(x, y, size):
    if size == 1:
        return

    new_size = size // 3
    for i in range(x + new_size, x + new_size * 2):
        for j in range(y + new_size, y + new_size * 2):
            sqr[i][j] = ' '

    for dx in range(3):
        for dy in range(3):
            if dx == 1 and dy == 1:
                continue  # 가운데는 이미 비움
            erase(x + dx * new_size, y + dy * new_size, new_size)

erase(0, 0, N)

for row in sqr:
    print("".join(row))
