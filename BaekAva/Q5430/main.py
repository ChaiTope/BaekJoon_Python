import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    cmds = input().rstrip()          # R/D 명령 문자열
    n = int(input())                 # 배열 길이
    arr_str = input().rstrip()       # "[x1,x2,...,xn]"

    # 배열 파싱
    if n:
        arr = deque(map(int, arr_str[1:-1].split(',')))
    else:
        arr = deque()

    rev = False      # 뒤집기 상태 플래그
    error = False

    # 명령 처리
    for c in cmds:
        if c == 'R':
            rev = not rev
        else:  # 'D'
            if not arr:
                print("error")
                error = True
                break
            if rev:
                arr.pop()
            else:
                arr.popleft()

    if error:
        continue

    # 최종 출력
    if rev:
        arr.reverse()
    print('[' + ','.join(map(str, arr)) + ']')
