import sys
input = sys.stdin.readline

N = int(input())
length = int(input())
s = input().rstrip()

target = 2 * N + 1  # P_N 패턴 길이 = I(OI)^N 길이

count = 0
i = 0
M = len(s)

while i + 2 < M:
    # “IOI”가 연속되는 구간 길이 세기
    if s[i] == 'I' and s[i+1] == 'O' and s[i+2] == 'I':
        run = 0
        # 연속되는 “IOI” 개수(run)를 셈
        while i + 2 < M and s[i] == 'I' and s[i+1] == 'O' and s[i+2] == 'I':
            run += 1
            i += 2  # 다음 “I” 자리로 점프
        # run번 반복된 “IOI” 구간이 있으니,
        # 여기서 P_N 패턴은 “IOI”가 N번 반복되는 것 => run >= N일 때 (run - N + 1)개가 만들어짐
        if run >= N:
            count += run - N + 1
    else:
        i += 1

print(count)
