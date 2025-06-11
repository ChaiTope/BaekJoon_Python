import sys
import heapq

# 1) 삽입
def insert(x):
    heapq.heappush(min_heap, x)
    heapq.heappush(max_heap, -x)
    counter[x] = counter.get(x, 0) + 1

# 2) 최솟값 꺼내기
def pop_min():
    while min_heap:
        x = min_heap[0]
        if counter.get(x,0) > 0:
            counter[x] -= 1
            return heapq.heappop(min_heap)
        heapq.heappop(min_heap)  # 이미 삭제된 항목 스킵
    return None  # 비어있음

# 3) 최댓값 꺼내기
def pop_max():
    while max_heap:
        x = -max_heap[0]
        if counter.get(x,0) > 0:
            counter[x] -= 1
            return -heapq.heappop(max_heap)
        heapq.heappop(max_heap)
    return None

# **peek용 함수** (꺼내지 않고, 유효한 최솟값/최댓값 확인)
def peek_min():
    while min_heap and counter.get(min_heap[0], 0) == 0:
        heapq.heappop(min_heap)
    return min_heap[0] if min_heap else None

def peek_max():
    while max_heap and counter.get(-max_heap[0], 0) == 0:
        heapq.heappop(max_heap)
    return -max_heap[0] if max_heap else None

input = sys.stdin.readline

T = int(input())

for i in range(T):
    min_heap, max_heap = [], []
    counter = {}   # {값: 남은 개수}

    n = int(input())

    for j in range(n):
        act, N = input().split()

        if act == 'I':
            insert(int(N))
        elif act == 'D':
            if N == '-1':
                pop_min()
            else:
                pop_max()

    # **peek으로만 확인** (counter나 힙 구조는 그대로 둠)
    mn = peek_min()
    mx = peek_max()
    if mn is None:  # 둘 다 None 이거나 하나라도 None 이면 empty
        print("EMPTY")
    else:
        print(mx, mn)