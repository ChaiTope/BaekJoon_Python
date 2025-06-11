import heapq

min_heap, max_heap = [], []
counter = {}   # {값: 남은 개수}

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
