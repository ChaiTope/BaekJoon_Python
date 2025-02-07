# 알파벳 대문자 로 이루어 진 단어가 주어 진다.
# ABC 는 3 이후로 3개씩 1씩 늘어 나고, PQRS는 8, TUV는 9, WXYZ는 10 <<이거 잘못 봐서 20분 날림
# A = 65 Z = 90
S = input()
Total = 0
for i in range(len(S)):
    if S[i] not in "PQRSTUVWXYZ":
        Total+=((ord(S[i]) - 65) // 3) + 3
    elif S[i] in "PQRS":
        Total+=8
    elif S[i] in "TUV":
        Total+=9
    else:
        Total+=10
print(Total, end="")