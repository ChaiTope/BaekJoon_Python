# Silver 3

## 문제
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

N개의 자연수 중에서 M개를 고른 수열
## 입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

## 출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

## Thinking!!
N, M 각 입력 받는 숫자 수, 출력할 숫자 자릿수

## 1차 시도
    import sys
    from collections import deque
    
    input = sys.stdin.readline
    
    N, M = map(int, input().split())
    
    nums = sorted(list(map(int, input().split())))
    
    dq = deque(sorted(nums))
    
    def backtrack(path, dq):
        if len(path) == M:
            print(*path)
            return
    
        for _ in range(len(dq)):
            x = dq.popleft()
            backtrack(path + [x], dq.copy())  # ← 복사본으로 넘김
            dq.append(x)
    
    backtrack([], dq)

# 2차 시도
    import itertools
    import sys
    
    input = sys.stdin.readline
    
    N, M = map(int, input().split())
    
    nums = sorted(list(map(int, input().split())))
    for comb in itertools.permutations(nums, M):
        print(*comb)
내장함수를 사용하면 간단함