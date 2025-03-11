while True:
    n = input()
    if n == ".":
        break
    stack = []
    for i in n:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if stack:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(")")
                    break
            else:
                stack.append(")")
                break
        elif i == "]":
            if stack:
                if stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append("]")
                    break
            else:
                stack.append("]")
                break
    if stack or n[-1] != ".":
        print("no")
    else:
        print("yes")
