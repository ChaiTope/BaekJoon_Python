# 한 줄에 최대 15개로 구성된 2차원 배열
# 이 2차원 배열을 세로로 읽어라, 빈 곳은 공백 으로 처리 한다.
# 세로로 읽은 순서 대로 공백 없이 출력

arr = [list(input().strip()) for _ in range(5)] # 한 줄씩 문자열 을 리스트 로 변환 .strip()
for i in range(15):
    for j in range(5):
        try:
            if i < len(arr[j]):
                print(arr[j][i], end='')
                continue
        except IndexError:
            continue


"""GPT 의 개선 코드"""
arr = [list(input().strip()) for _ in range(5)]  # 입력을 리스트로 변환

for i in range(15):
    for j in range(5):
        if i < len(arr[j]):  # ✅ 배열 길이 체크만으로 안전한 접근 가능
            print(arr[j][i], end='')  # ✅ 세로 읽기 출력

"""
이미 배열 길이를 체크했기 때문에 try-except 구문이 필요하지 않음
어차피 자동반복 되므로 continue도 필요하지 않음
"""