import sys

input = sys.stdin.readline

T = input().rstrip()
P = input().rstrip()

def build_lps(pattern):
    m = len(pattern)
    lps = [0] * m

    j = 0                 # 지금까지 일치한 접두사 길이

    for i in range(1, m):  # i는 오른쪽으로 쭉 진행
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j-1]  # j를 한 단계 줄이기 (이전 접두사 길이)

        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j    # i 위치까지의 최대 접두사==접미사 길이 저장

    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = build_lps(pattern)

    result = []
    j = 0

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j-1]

        if text[i] == pattern[j]:
            if j == m-1:
                result.append(i - m + 2)  # 1-based
                j = lps[j]
            else:
                j += 1

    return len(result), result

times, res = kmp_search(T, P)

print(times)
if times > 0:
    print(*res)