N = int(input())

people = set()
count = 0

for _ in range(N):
    name = input()
    if name == "ENTER":
        people.clear()
    elif name not in people:
        people.add(name)
        count += 1

print(count)