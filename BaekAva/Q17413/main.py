import sys

input = sys.stdin.readline

array = input().rstrip()
i = 0
is_tag = False
stack = []

while i < len(array):
    if is_tag:
        stack.append(array[i])
        if array[i] == '>':
            is_tag = False
            print("".join(stack), end="")
            stack = []
        i += 1

    elif array[i] == '<':
        print("".join(reversed(stack)), end="")
        stack = []
        is_tag = True
        stack.append(array[i])
        i += 1

    elif array[i] == ' ':
        print("".join(reversed(stack)), end=" ")
        stack = []
        i += 1

    else:
        stack.append(array[i])
        i += 1

# 루프 끝난 뒤 남은 문자 처리
if stack:
    if is_tag:
        print("".join(stack), end="")
    else:
        print("".join(reversed(stack)), end="")
