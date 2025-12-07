import sys

input = sys.stdin.readline

start = 1
end = int(input())
p = 1
cnt = [0] * 10

def add(x, p):
    while x > 0:
        digit = x % 10       # 맨 뒤 자리
        cnt[digit] += p
        x //= 10             # 다음 자리로 이동


while start <= end:
    # 1) 왼쪽 정리
    while start % 10 != 0 and start <= end:
        add(start, p)
        start += 1

    # 여기서 범위가 다 닳아버리면 끝
    if start > end:
        break

    # 2) 오른쪽 정리
    while end % 10 != 9 and start <= end:
        add(end, p)
        end -= 1

    # 3) 가운데 블록 처리
    block_cnt = (end - start + 1) // 10   # ← 정수 나눗셈 꼭 // !!
    for d in range(10):
        cnt[d] += block_cnt * p

    # 4) 다음 자리로 이동
    start //= 10
    end   //= 10
    p    *= 10

print(*cnt)