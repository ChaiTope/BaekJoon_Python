import sys
input = sys.stdin.readline
write = sys.stdout.write

# 1) 문장 입력받고 개행 제거
sentence = input().rstrip()
L = len(sentence)

# 2) 26글자 × (L+1) 크기의 누적합 배열 생성
ps = [[0] * (L + 1) for _ in range(26)]

# 3) prefix sum 채우기
for i, ch in enumerate(sentence):
    ci = ord(ch) - ord('a')
    # 이전 값 그대로 복사
    for j in range(26):
        ps[j][i + 1] = ps[j][i]
    # 해당 문자 하나 증가
    ps[ci][i + 1] += 1

# 4) 쿼리 처리
N = int(input())
for _ in range(N):
    letter, s, e = input().split()
    s, e = int(s), int(e)
    ci = ord(letter) - ord('a')
    cnt = ps[ci][e + 1] - ps[ci][s]
    write(str(cnt) + '\n')
