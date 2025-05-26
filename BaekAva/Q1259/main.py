while True:
    nums = input()

    if nums == '0':
        break
    N = list(map(int, nums))

    if N == list(reversed(N)):
        print("yes")
    else:
        print("no")