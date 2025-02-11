# 팰린드롬인지 확인 하기
S = input()
print(int(S == S[::-1]))

print(int(input() == input()[::-1])) # << input 자체가 값을 입력 받는 함수라 값을 두번 입력 받음.