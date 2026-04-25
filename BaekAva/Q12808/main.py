import sys
input = sys.stdin.readline

def make(total, cnt):
    if cnt == 0:
        return [] if total == 0 else None
    if total < cnt:
        return None
    arr = [1] * cnt
    arr[0] += total - cnt
    return arr

def solve(a, b, c, d):
    if abs(b - c) > 1:
        return "impossible"

    if b == 0 and c == 0:
        if a and d:
            return "impossible"
        if a:
            return "0" * (a + 1)
        if d:
            return "1" * (d + 1)
        return "0"

    if b == c:
        cases = [(b + 1, b, 0), (b, b + 1, 1)]
    elif b == c + 1:
        cases = [(b, b, 0)]
    else:
        cases = [(c, c, 1)]

    for zn, on, st in cases:
        z = a + zn
        o = d + on

        zb = make(z, zn)
        ob = make(o, on)

        if zb is None or ob is None:
            continue

        res = []

        if st == 0:
            for i in range(on):
                res.append("0" * zb[i])
                res.append("1" * ob[i])
            if zn > on:
                res.append("0" * zb[-1])
        else:
            for i in range(zn):
                res.append("1" * ob[i])
                res.append("0" * zb[i])
            if on > zn:
                res.append("1" * ob[-1])

        return "".join(res)

    return "impossible"

t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    print(solve(a, b, c, d))