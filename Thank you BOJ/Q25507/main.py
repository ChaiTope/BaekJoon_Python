import sys

input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    # a, b, c, p, 지식, 구현력, 사고력, d-day // d - 실행한 계획, q - 남은 스탯
    board = [list(map(int, input().split())) for _ in range(N)]
    a=b=c=d=p=q=0
    F = True

    for row in board:
        # 목표 능력치 + 현재 시간
        xa, xb, xc, xp = row

        # 필요 능력치 + 여유 시간(실행 할 때는 능력치 증가 불가)
        # 필요 스탯이 원래 스탯 보다 낮을 때를 고려 해서 max() 사용
        # 필요 시간이 원래 시간과 같을 때를 고려해 max() 사용
        na = max(0, xa - a)
        nb = max(0, xb - b)
        nc = max(0, xc - c)

        # 필요한 스탯, 남는 스탯
        need = na + nb + nc
        free = q + (xp - p)

        # 만약 필요 스탯 + 1 이 남은 스탯 보다 크면
        if need + 1 > free:
            F = False
            break

        # 남는 스탯 갱신
        q = free - need - 1

        a, b, c, p = max(a, xa), max(b, xb), max(c, xc), max(p, xp)

        # 누적 작업 수 갱신
        d += 1
    if F:
        print("YES")
    else:
        print("NO")