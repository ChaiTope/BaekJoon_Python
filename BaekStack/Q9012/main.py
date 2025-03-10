n = int(input())
for _ in range(n):
    p = input()
    stack = []
    for i in p:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack:
                stack.pop()
            else:
                stack.append(")")
                break

    if stack:
        print("NO")
    else:
        print("YES")
