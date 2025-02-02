a = int(input())
for i in range(1, a+1):
    print("*" * i)

"""
GPT의 다른 정답
print("\n".join("*" * i for i in range(1, int(input()) + 1)))
.join을 이용한 코드 최적화
<< 하지만 GPT도 마지막 줄바꿈을 캐치하지 못함 ,end=""를 누락
"""