# Silver 3

# 문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.
## 입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

## 출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

## Thinking!!
이전문제랑 다른건 이미 한번 모양만 다른 중복수열은 제거해야함
근데 이 조합 문제는 그냥 itertools의 combinations를 사용하면 됨

하지만? 백트래킹과 재귀를 사용해서 풀어봄

## combinations 함수 사용 안한 코드

    def backtrack(start, path):
        if len(path) == M:
            print(' '.join(map(str, path)))
            return
        
        for i in range(start, N + 1):
            path.append(i)
            backtrack(i + 1, path)  # i+1부터 시작 (중복 방지 + 오름차순)
            path.pop()
    
    N, M = map(int, input().split())
    backtrack(1, [])

