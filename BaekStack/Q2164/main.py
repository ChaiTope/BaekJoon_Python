from collections import deque

n = int(input())

cards = []
for i in range(n):
    cards.append(i+1)

cards = deque(reversed(cards))

while len(cards) > 1:
    print(cards)
    cards.pop()
    cards.appendleft(cards.pop())

print(cards)