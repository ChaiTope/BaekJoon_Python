import sys
from collections import namedtuple

input = sys.stdin.readline

Person = namedtuple("Person", ["weight", "height"])

N = int(input())
people = []

for i in range(N):
    p = Person(*map(int, input().split()))
    people.append(p)

price = [0] * N
for i in range(N):
      cnt = 0
      for j in range(N):
          if i == j: continue
          if people[j].weight > people[i].weight and people[j].height > people[i].height:
              cnt += 1
      price[i] = cnt + 1

print("\n".join(map(str, price)))