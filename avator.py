from collections import Counter

for i in range(3):
    arr = Counter(list(map(int, input().split())))
    print({1:"A", 2:"B", 3:"C", 4:"D", 0:"E"}[arr[0]])