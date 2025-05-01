import sys
from math import gcd

input = sys.stdin.readline

n = int(input())
prev_total = 0          # 이전 로그의 total을 저장
m = 0                   # 누적 GCD(최종 M)
max_remain = 0          # 충전 직후의 total 중 최대값

for _ in range(n):
    money, total = map(int, input().split())

    # — 충전 없이 처리된 경우(입금이거나 출금 후 잔액 ≥ 0)
    if prev_total + money >= 0:
        # 로그상의 total이 일치해야 함
        if total != prev_total + money:
            print(-1)
            sys.exit()
    else:
        # — 부족해서 충전이 발생한 경우
        diff = total - (prev_total + money)
        # diff는 무조건 양수여야 함
        if diff <= 0:
            print(-1)
            sys.exit()
        # diff마다 GCD 누적
        m = gcd(m, diff)
        # 충전 후 남은 잔액(=total)을 기록
        max_remain = max(max_remain, total)

    # 이전 잔액 갱신
    prev_total = total

# — 충전 로그가 하나도 없으면 가능한 M이 무수히 많으므로 1을 출력
if m == 0:
    print(1)
    sys.exit()

# — 충전 후 남은 잔액이 M 이상이면 “한 번만 충전” 조건 위배
if max_remain >= m:
    print(-1)
else:
    print(m)
