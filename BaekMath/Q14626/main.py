isbn = input().rstrip()
summary = 0
star = isbn.index('*')
weight = 1 if star % 2 == 0 else 3

for i, ch in enumerate(isbn):
    if ch == '*': continue
    digit = int(ch)
    summary += digit if i % 2 == 0 else digit * 3

for d in range(10):
    if (summary + weight*d) % 10 == 0:
        print(d)
        break