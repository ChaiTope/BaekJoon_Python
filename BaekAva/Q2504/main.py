s = input().strip()
stack = []

for ch in s:
    if ch == '(' or ch == '[':
        stack.append(ch)

    elif ch == ')':
        if not stack:
            print(0)
            exit()

        temp = 0

        while stack and isinstance(stack[-1], int):
            temp += stack.pop()

        if not stack or stack[-1] != '(':
            print(0)
            exit()

        stack.pop()

        if temp == 0:
            stack.append(2)
        else:
            stack.append(temp * 2)

    elif ch == ']':
        if not stack:
            print(0)
            exit()

        temp = 0

        while stack and isinstance(stack[-1], int):
            temp += stack.pop()

        if not stack or stack[-1] != '[':
            print(0)
            exit()

        stack.pop()

        if temp == 0:
            stack.append(3)
        else:
            stack.append(temp * 3)

for x in stack:
    if x == '(' or x == '[':
        print(0)
        exit()

print(sum(stack))