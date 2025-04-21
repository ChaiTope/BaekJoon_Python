N = int(input())
signs = input().split()
visited = [False] * 10
max_ans = ''
min_ans = ''

def valid(a, b, sign):
    if sign == '<':
        return a < b
    else:
        return a > b

def backtrack(depth, path):
    global max_ans, min_ans

    if depth == N + 1:
        num_str = ''.join(map(str, path))
        if not min_ans:
            min_ans = num_str
        else:
            max_ans = num_str
        return

    for i in range(10):
        if not visited[i]:
            if depth == 0 or valid(path[-1], i, signs[depth - 1]):
                visited[i] = True
                path.append(i)
                backtrack(depth + 1, path)
                path.pop()
                visited[i] = False

backtrack(0, [])
print(max_ans)
print(min_ans)
