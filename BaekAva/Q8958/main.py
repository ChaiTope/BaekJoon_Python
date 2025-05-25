T = int(input())

for i in range(T):
    ox = input()
    count = 0
    summary = 0
    for j in range(len(ox)):
        if ox[j] == "O":
            count += 1
            summary += count
        else:
            count = 0

    print(summary)