# 전공평점을 계산해보자!
# 전공평점은 (학점 * 과목평점) 의 합을 학점의 총 합으로 나눈 것
# 20줄에 걸쳐 과목명, 학점, 등급이 공백으로 구분되어 주어진다.
lec  = 0
avg = 0
for _ in range(20):
    name,point, grade = input().split()
    if grade == "F": grade = 0
    elif grade == "D0": grade = 1
    elif grade == "D+": grade = 1.5
    elif grade == "C0": grade = 2
    elif grade == "C+": grade = 2.5
    elif grade == "B0": grade = 3
    elif grade == "B+": grade = 3.5
    elif grade == "A0": grade = 4
    elif grade == "A+": grade = 4.5
    elif grade == "P":
        continue
    lec += float(point)
    avg += (float(grade) * float(point))

print(avg/lec)

"""GPT 의 개선 코드"""
grade_dict = {
    "A+": 4.5, "A0": 4.0,
    "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0,
    "D+": 1.5, "D0": 1.0,
    "F": 0.0
}

lec = 0
avg = 0

for _ in range(20):
    name, point, grade = input().split()

    if grade == "P":  # Pass 과목은 무시
        continue

    lec += float(point)
    avg += float(point) * grade_dict[grade]  # 딕셔너리 활용!

print(avg / lec)
"""
dict{} 를 사용 하면 훨씬 더 빠른 실행이 가능
# 1️⃣ 딕셔너리 선언 (조건: 결과 형태)
grade_dict = {
    "A+": 4.5, "A0": 4.0,
    "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0,
    "D+": 1.5, "D0": 1.0,
    "F": 0.0
}

# 2️⃣ 값을 가져올 때 → 변수명[키]
print(grade_dict["A+"])  # 4.5 출력
print(grade_dict["B0"])  # 3.0 출력

# 3️⃣ 변수로 키 값을 넣어서 조회 가능
grade = "C+"
print(grade_dict[grade])  # 2.5 출력
"""