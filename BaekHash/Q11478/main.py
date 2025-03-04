S = input().strip()
substrings = set()

for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        substrings.add(S[i:j])

print(len(substrings))