import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cnt = [0] * M
cnt[0] = 1   # 빈 구간(0~i) 자체가 M으로 나누어 떨어지는 경우를 미리 세어두기

s = 0
ans = 0
for x in map(int, input().split()):
    s = (s + x) % M
    ans += cnt[s]   # 지금까지 같은 나머지가 나온 횟수만큼 (i,j) 구간이 만들어짐
    cnt[s] += 1     # 나머지 s 가 앞으로 또 등장할 수 있도록 카운트

print(ans)
