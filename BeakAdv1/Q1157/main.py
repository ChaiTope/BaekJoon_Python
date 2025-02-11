#영어로 된 문자열을 입력받고, 가장 많이 입력받은 문자를 출력하라, 대소문자 비교 없이.
#아스키코드로 for문 돌려서 같은거 찾을때마다 카운트 올리고 그걸 배열에 넣어야하나?
S = input()
count = [0] * 26
m_count = 0
m_char = ""
for i in range(97, 123):
    if chr(i) in S:
        count[i - 97] += S.count(chr(i))

for j in range(65, 91):
    if chr(j) in S:
        count[j - 65] += S.count(chr(j))

for h in range(len(count)):
    if count[h] == max(count): # 만약 카운트의 가장 큰 값이 카운트 반복중 해당 값과 같으면 실행
        m_count += 1
        m_char = chr(h + 65)
        if m_count > 1:
            m_char = "?"
            break

print(m_char)

"""GPT 의 개선 코드"""
S = input().upper()  # 전부 대문자로 변환 << 이게 말이 안됨 그냥 생각도 못했음
count = [0] * 26  # A-Z 카운트 저장할 리스트

# 문자열 순회하며 알파벳 개수 카운트
for char in S:
    count[ord(char) - 65] += 1 # 그냥 카운트 하나로 처리함 upper 을 사용 해서 가능한 방법임

# 최댓값 찾기
max_count = max(count)
m_char = '?' if count.count(max_count) > 1 else chr(count.index(max_count) + 65)

print(m_char)