import sys
import copy

input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
directions = ["L", "R", "U", "D"]
ans = 0

def get_line(axis, idx, n_map):
    if axis == 0: # 가로면
        line = [n_map[idx][c] for c in range(N)]

    else:
        line = [n_map[r][idx] for r in range(N)]

    return line

def merge(line):
    vals = []
    res_line = []

    for i in range(N):
        if line[i] != 0:
            vals.append(line[i])

    i = 0

    while i < len(vals):
        if i+1 < len(vals) and vals[i] == vals[i+1]:
            res_line.append(vals[i]*2)
            i += 2
        else:
            res_line.append(vals[i])
            i += 1

    return res_line + [0] * (N - len(res_line))

def set_line(axis, idx, n_map, line):
    if axis == 0:
        n_map[idx] = line
    else:
        for r in range(N):
            n_map[r][idx] = line[r]

def move(n_map, d):
    if d == "L":
        for r in range(N):
            line = get_line(0, r, n_map)
            m_line = merge(line)
            set_line(0, r, n_map, m_line)
    elif d == "R":
        for r in range(N):
            line = get_line(0, r, n_map)[::-1]
            m_line = merge(line)[::-1]
            set_line(0, r, n_map, m_line)
    elif d == "D":
        for c in range(N):
            line = get_line(1, c, n_map)[::-1]
            m_line = merge(line)[::-1]
            set_line(1, c, n_map, m_line)
    elif d == "U":
        for c in range(N):
            line = get_line(1, c, n_map)
            m_line = merge(line)
            set_line(1, c, n_map, m_line)

def dfs(depth, maps):
    global ans
    m_val = max(list(map(max, maps)))
    ans = max(ans, m_val)
    if depth == 5:
        return

    for direction in directions:
        new_maps = copy.deepcopy(maps)
        move(new_maps, direction)
        dfs(depth+1, new_maps)

dfs(0, board)
print(ans)