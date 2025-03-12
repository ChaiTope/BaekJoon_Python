import sys
from collections import deque

n = int(input())
deck = deque()
for i in range(n):
    d = sys.stdin.readline().split()

    if d[0] == "1":
        deck.appendleft(d[1])

    elif d[0] == "2":
        deck.append(d[1])

    elif d[0] == "3":
        print(deck.popleft() if deck else -1)

    elif d[0] == "4":
        print(deck.pop() if deck else -1)

    elif d[0] == "5":
        print(len(deck))

    elif d[0] == "6":
        print(0 if deck else 1)

    elif d[0] == "7":
        print(deck[0] if deck else -1)

    elif d[0] == "8":
        print(deck[-1] if deck else -1)