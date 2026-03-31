T = int(input())
A = [list(input()) for _ in range(T)]

for i in range(T):
    sl, sr = [], []

    for ch in A[i]:
        if ch == '<':
            if sl:
                sr.append(sl.pop())

        elif ch == '>':
            if sr:
                sl.append(sr.pop())

        elif ch == '-':
            if sl:
                sl.pop()

        else:
            sl.append(ch)

    print(''.join(sl + sr[::-1]))