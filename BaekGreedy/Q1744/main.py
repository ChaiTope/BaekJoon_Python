N = int(input())
A = sorted([int(input()) for _ in range(N)])
under = []
upper = []
zero = []
one = []
res = []

def categorize(path):
    while path:
        a = path.pop()
        if a > 1:
            upper.append(a)
        elif a == 1:
            one.append(a)
        elif a == 0:
            zero.append(a)
        else:
            under.append(a)

def judge(path):
    if len(path) % 2 == 1:
        a = path.pop()
        if not zero or a > 0:
            res.append(a)

def get_res(path):
    judge(path)

    while path:
        n, m = path.pop(), path.pop()
        res.append(n*m)

categorize(A)
under = sorted(under)
get_res(upper)
get_res(under)
res.append(sum(one))

print(sum(res))