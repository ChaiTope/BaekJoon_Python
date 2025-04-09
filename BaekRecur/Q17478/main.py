N = int(input())

text1 = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."

text2 = "\"재귀함수가 뭔가요?\""

text3 = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."

text6 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."

text7 = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""

text4 = "라고 답변하였지."

text5 = "\"재귀함수는 자기 자신을 호출하는 함수라네\""

count = 0
def recursion(n):
    global count
    if n == 0:
        print("____"*count + text2)
        print("____"*count + text5)
        print("____"*count + text4)
        return


    print("____"*count + text2)
    print("____"*count + text3)
    print("____"*count + text6)
    print("____"*count + text7)
    count += 1
    recursion(n - 1)
    count -= 1
    if count == 0:
        print(text4, end="")
    else:
        print("____"*count + text4)

print(text1)
recursion(N)