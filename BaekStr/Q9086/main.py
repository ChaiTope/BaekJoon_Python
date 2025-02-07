# 테스트 횟수 N을 입력 받는다.
# 그 횟수 만큼 문자열 을 입력 받는다.
# 받은 문자열 들의 첫 글자와 끝 글자만 매 줄 출력 한다.
N = int(input())
Arr = []
for i in range(N):
    Arr.append(input())
for i in range(N):
    if i != N-1:
        print(Arr[i][0]+Arr[i][-1])
    else:
        print(Arr[i][0]+Arr[i][-1], end="")
        break

""" GPT 가 최적화 """
N = int(input())
arr = [input() for _ in range(N)]  # ✅ 입력을 한 번에 리스트로 저장

print("\n".join(s[0] + s[-1] for s in arr))  # ✅ 출력도 한 번에 처리!

""" 아니 리스트 컴프리헨션 이거 진짜 기억 하기 빡세네 """