import sys

a = int(sys.stdin.readline().strip()) # 개행 문자 제거
res = []
for i in range(a):
    b, c = map(int, sys.stdin.readline().split())
    res.append(b + c)

for j in range(a):
    print(res[j])

"""
input()보다 sys.stdin.readline()이 더 빠르다
why?
📌 sys.stdin.readline()은 C 기반의 "버퍼 입력"을 사용해서 input()보다 빠름!
📌 input()은 내부적으로 추가적인 처리가 들어가서 상대적으로 느림!
"""