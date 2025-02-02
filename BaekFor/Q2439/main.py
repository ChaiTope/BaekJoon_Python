#별을 오른쪽 정렬로 찍기
a = int(input())
for i in range(1, a+1):
    print(" " * (a-i), end="")
    print("*" * i)


"""
스스로 최적화 해보기
추가로 배운 점, "\n".join을 하면 마지막 출력 후에도 줄바꿈을 하기 때문에 반드시 end=""를 붙이자
"""
a = int(input())
print("\n".join(" " * (a-i) + "*" * i for i in range(1, a+1)), end="")


"""
GPT의 도움
.join 은 하나의 반복 가능한 객체만 받기 때문에
여러 개의 다른 패턴을 합칠 땐 + 를 로 조합 하기!!
"""