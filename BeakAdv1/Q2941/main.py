# 크로아티아 알파벳의 갯수를 구하자
A = ["c=","c-","dz=","d-","lj","nj","s=","z="]
S = list(input())
cnt = len(S)
for i in range(len(S)-1):
    for j in range(len(A)):
        if S[i] + S[i+1] == A[j]:
            cnt-=1
            i+=1
            break
for i in range(len(S)-2):
    for j in range(len(A)):
        if S[i] + S[i+1] + S[i+2] == A[j]:
            cnt-=1
            i+=2
            break
print(cnt)

"""GPT 의 개선 코드"""
A = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
S = input()
cnt = 0
i = 0

while i < len(S):
    if S[i:i+3] in A:  # "dz=" 같은 3글자 크로아티아 알파벳 체크
        cnt += 1
        i += 3
    elif S[i:i+2] in A:  # 2글자 크로아티아 알파벳 체크
        cnt += 1
        i += 2
    else:  # 일반 문자
        cnt += 1
        i += 1

print(cnt)
"""
추가로 안 지식.
인덱스 슬라이싱([i:i+a])은 슬라이싱 범위를 벗어 나면
그 다음 범위는 공백(" ")으로 채워지기 때문에
index 에러가 발생 하지 않는다.
"""