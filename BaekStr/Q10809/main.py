# 첫 줄에 단어 S 가 주어 진다.
# a ~ z 까지 단어가 포함 되면 포합 된 앞에서 첫 번째 위치를 a 부터 순서 대로 숫자로 출력
# 만약 없으면 -1, 첫 번째 순서를 0 으로 한다.

S = input()
for i in range(97, 123):
    if chr(i) in S:
        print(S.index(chr(i)), end=" ")
    else:
        print(-1, end=" ")
print("\b", end="")

# join 사용을 생활화 하자!

S = input()
print(" ".join(str(S.index(chr(i))) if chr(i) in S else "-1" for i in range(97, 123)))

# 문자열 로 변환.S의 유니 코드(i)가 있으면.만약 유니 코드(i) 가 배열 S 안에 있으면 -1.i를 97부터 122까지 반복