import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def build_stars(n):
    # 재귀의 기저 사례: n == 3일 때
    if n == 3:
        return ["  *  ",
                " * * ",
                "*****"]
    # 절반 크기의 패턴을 먼저 구함
    prev = build_stars(n // 2)
    top = [ " " * (n // 2) + line + " " * (n // 2) for line in prev ]
    bottom = [ line + " " + line for line in prev ]
    return top + bottom

N = int(input().rstrip())
art = build_stars(N)
# 출력
print("\n".join(art))
