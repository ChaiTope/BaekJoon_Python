# 과목의 수 N을 입력 받고, 그 수 만큼 수를 공백 으로 구분 해서 1줄 로 입력 받는다.
# 받은 점수 중 최대값 M, 모든 점수를 점수/M*100으로 수정 하여 평균을 출력 한다.

N = int(input())
arr = list(map(int, input().split()))
evg = []
for i in range(N):
    evg.append((arr[i]/max(arr))*100)
print (sum(evg)/N)

"""GPT 의 최적화"""

N = int(input())
arr = list(map(int, input().split()))
M = max(arr)  # ✅ 최댓값 저장
evg = [(x / M) * 100 for x in arr]  # ✅ 리스트 컴프리헨션 활용

print(sum(evg) / N)  # ✅ 평균 출력

""" 또는 """

N = int(input())
arr = list(map(int, input().split()))
print(sum(x / max(arr) * 100 for x in arr) / N)  # ✅ 한 줄로 해결!