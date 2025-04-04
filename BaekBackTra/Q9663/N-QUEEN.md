# Gold 4

## 문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

## 입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

## 출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

## Thinking!!
같은 row가 아니며, row+col, row-col이 같지 않는 경우에 배치해야 한다

"row는 재귀로 하나씩 내려가고, col은 반복문으로 0~N-1을 돌면서 유효한 자리에 퀸을 놓는다"

## 1차 시도

    import sys
    
    input = sys.stdin.readline
    print = sys.stdout.write
    
    def placequeen(row, queens):
        global Q_count
        if row == N:
            Q_count += 1
            return
    
        for col in range(N):
            if is_safe(row, col, queens):
                queens.append(col)
                placequeen(row + 1, queens)
                queens.pop()
    
    def is_safe(row, col, queens):
        for i in range(row):
            if queens[i] == col or abs(queens[i] - col) == abs(i - row):
                return False
        return True
    
    N = int(input().strip())
    
    Q_count = 0
    
    placequeen(0, [])
    
    print(str(Q_count))

queens 리스트를 매번 append, pop 하면서 is_safe()에서 모든 행을 전부 검사하고 있기 때문에
15일 때 시간초과가 일어나는 것 같음
(현재 코드의 시간 복잡도는 O(N! * N)수준)

따라서 for로 검사하지 않고, set이나 list로 퀸이있는 열과 행만 찾아봄

수정본이 본문 코드