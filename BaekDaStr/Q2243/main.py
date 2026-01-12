import sys
input = sys.stdin.readline

MAX = 1000000

# Fenwick Tree (1-indexed)
tree = [0] * (MAX + 1)

def add(i: int, delta: int):
    """i번 인덱스에 delta 더하기"""
    while i <= MAX:
        tree[i] += delta
        i += i & -i

def prefix_sum(i: int) -> int:
    """1..i 누적합"""
    s = 0
    while i > 0:
        s += tree[i]
        i -= i & -i
    return s

def kth(k: int) -> int:
    """
    누적합 기준으로 k번째 원소가 위치한 인덱스(맛 번호) 찾기
    (tree 전체 합 >= k 가 보장된 상황에서 호출)
    """
    idx = 0
    bit = 1 << 20  # 2^20 = 1,048,576 >= 1,000,000

    while bit:
        nxt = idx + bit
        if nxt <= MAX and tree[nxt] < k:
            k -= tree[nxt]
            idx = nxt
        bit >>= 1
    return idx + 1

# ----- main skeleton -----
N = int(input())
out = []

for _ in range(N):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        # 1 B : B번째 사탕 꺼내기
        B = cmd[1]
        taste = kth(B)
        out.append(str(taste))
        add(taste, -1)   # 꺼냈으니 1개 감소
    else:
        # 2 B C : B맛 사탕 C개 추가(또는 감소)
        B, C = cmd[1], cmd[2]
        add(B, C)

print("\n".join(out))