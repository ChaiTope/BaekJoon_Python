n = int(input())
stack = []
for i in range(n):
    k = int(input())
    if k != 0:
        stack.append(k)
    else:
        stack.pop()

if stack:
    print(sum(stack))
else:
    print(0)