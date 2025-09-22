import sys

input = sys.stdin.readline

string = input().rstrip()

bomb = list(input().rstrip())

stack = []

for ch in string:
    stack.append(ch)  # 하나씩 넣기

    # stack의 끝부분이 bomb와 길이가 같거나 더 클 때만 검사
    if len(stack) >= len(bomb):
        # stack의 끝부분이 bomb와 동일하면 pop
        if stack[-len(bomb):] == bomb:
            for _ in range(len(bomb)):
                stack.pop()

result = ''.join(stack)
print(result if result else "FRULA")
