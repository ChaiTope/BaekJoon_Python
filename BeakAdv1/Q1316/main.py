# 그룹 단어의 갯수를 구하라. 그룹 단어란? 앞에 한번 나온 문자가 다시 나오지 않는 단어
C = int(input())
cnt = C
arr = 0

for _ in range(C):
    s = list(input())
    for i in range(len(s)-1): # 입력 받은 문자열 중 문자와 다음 문자 비교
        if s[i] != s[i+1]:
            for j in range(i+1,len(s)): # 다음 문자가 틀리면 그 문자 부터 끝 문자 까지 같은 게 있나 비교
                if s[i] in s[j:]: # 만약 같은 문자가 있으면?
                    arr+=1
                    break
    if arr >= 1: # 같은 문자가 있을 때(그룹 단어가 아닐 때) 그 단어는 아니니 -1 해줌
        cnt-=1
        arr = 0

print(cnt)

"""GPT가 개선해준 코드"""
C = int(input())
cnt = 0

for _ in range(C):
    S = input()
    seen = set()  # 등장한 문자 저장
    is_group = True  # 그룹 단어 여부

    for i in range(len(S)):
        if i > 0 and S[i] != S[i-1]:  # 이전 문자와 다르면 검사
            if S[i] in seen:  # 이미 나온 문자면 그룹 단어 아님
                is_group = False
                break
        seen.add(S[i])  # 현재 문자 저장

    if is_group:
        cnt += 1

print(cnt)

"""
set()은 뭔가?
set(집합)의 특징
중복을 자동으로 제거함
검색(in 연산)이 리스트보다 훨씬 빠름 (O(1))
순서가 없음 → 리스트처럼 인덱스로 접근 불가능 (set[0] ❌) << 순서가 보장되지 않음
"""