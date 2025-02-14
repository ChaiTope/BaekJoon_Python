# 미국식 거스름 돈 계산 하기
# 25 10 5 1 순서로 출력
# 첫 줄에 테스트 수, 이후에 거스름 할 돈 입력

T = int(input())
res = [[0] * 4 for i in range(T)]
for i in range(T):
    Exc = int(input())
    res[i][0] = (Exc//25)
    res[i][1] = ((Exc%25)//10)
    res[i][2] = (((Exc%25)%10)//5)
    res[i][3] = (((Exc%25)%10)%5)
for j in range(T):
    print(res[j][0], res[j][1], res[j][2], res[j][3])

"""GPT 의 개선 코드"""
import sys
input = sys.stdin.readline

T = int(input().strip())
results = []

for _ in range(T):
    Exc = int(input().strip())
    q, r = divmod(Exc, 25)  # 쿼터
    d, r = divmod(r, 10)    # 다임
    n, p = divmod(r, 5)     # 니켈, 페니
    results.append(f"{q} {d} {n} {p}")

# 결과 한 번에 출력
print("\n".join(results))

"""
f"{},{}" << 이거 잊고 있었다. 문자열 앞에 f 또는 F를 붙이면, 중괄호 {} 안에 변수나 표현식을 바로 넣을 수 있다.
name = "동혁"
age = 25

# f-string 사용
print(f"안녕, 내 이름은 {name}이고, 나이는 {age}살이야.")
이런 식으로 사용 가능 하다.
"""