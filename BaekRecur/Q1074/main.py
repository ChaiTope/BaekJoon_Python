n, r, c = map(int, input().split())

def z(n, r, c):
    if n == 0:
        return 0
    half = 2 ** (n - 1)
    block_size = half * half

    if r < half and c < half:
        return z(n - 1, r, c)
    elif r < half <= c:
        return block_size + z(n - 1, r, c - half)
    elif r >= half > c:
        return 2 * block_size + z(n - 1, r - half, c)
    else:
        return 3 * block_size + z(n - 1, r - half, c - half)

print(z(n, r, c))