S = input()
t = S[0]

z = 1 if t == '0' else 0
o = 1 if t == '1' else 0

for a in S[1:]:
    if a != t:
        t = a
        if a == "1":
            o += 1
        else:
            z += 1

print(min(z, o))