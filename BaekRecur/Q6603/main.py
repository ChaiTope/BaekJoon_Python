def recurse(depth, path):
    if len(path) == 6:
        print(" ".join(map(str, path)))
        return

    for i in range(depth, len(lotto)):
        path.append(lotto[i])
        recurse(i + 1, path)
        path.pop()


while True:
    array = list(map(int, input().split()))
    N = array[:1]
    lotto = array[1:]

    if N[0] == 0:
        break

    recurse(0, [])
    print()