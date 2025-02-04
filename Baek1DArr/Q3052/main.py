# 10 개의 수를 입력 받고, 42 로 나눈 나머지 를 구한다
# 그 다음 서로 다른 값이 몇 개인지 출력 한다.
arr = []
count = 0
for i in range(10):
    num = int(input())
    if num % 42 not in arr:
        arr.append(num % 42)
        count+=1
print(count)

""" GPT 를 이용한 최적화 코드 """
nums = {int(input()) % 42 for _ in range(10)}  # ✅ set을 사용하여 중복 제거
print(len(nums))  # ✅ 중복이 제거된 요소 개수 출력