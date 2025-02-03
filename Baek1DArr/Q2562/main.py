# 아홉 개의 100 이하의 자연수 를 입력 받는다
# 입력 받은 자연수 중 가장 큰 수와 그 수가 몇 번째에 입력 됐는지 출력 한다
num_list = []
for i in range(9):
    input_num = int(input())
    num_list.append(input_num)
for i in range(9):
    if num_list[i] == max(num_list):
        print(max(num_list))
        print(i+1)

"""GPT 의 개선"""
max_value = max(num_list)
for i in range(9):
    if num_list[i] == max_value:
        print(max_value)
        print(i+1)

"""index() 를 활용 하는 방법"""
num_list = [int(input()) for _ in range(9)]
max_value = max(num_list)
max_index = num_list.index(max_value)  # 0-based index
print(max_value)
print(max_index + 1)  # 문제에서는 1-based index이므로 +1 해줌

# index() 함수는 특정 값이 리스트 내에서 **처음 등장 하는 위치(인덱스)**를 반환