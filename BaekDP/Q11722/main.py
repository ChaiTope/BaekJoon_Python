max = 0
h = 0
for i in range(4):
    O, I = map(int, input().split())
    h = h + I - O
    if h > max:
        max = h
print(max)