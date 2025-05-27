# Silver 1

## 문제
정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

2를 곱한다.
1을 수의 가장 오른쪽에 추가한다. 
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

## 입력
첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진다.

## 출력
A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.

## Thinking!!
A에서 B로 2배를 하거나 수의 오른쪽에 1을 붙이거나.

### 함수로 해봤는데, 생각해보니까 함수로 할 필요가 없음
    path = []
    def search(A, B, count):
        if A == B:
            return path.append(count)
    
        if A < B:
            if B % 10 == 1:
                search(A, B // 10, count + 1)
            elif B % 2 == 0:
                search(A, B // 2, count + 1)
    
    search(A, B, 0)
    
    if path:
        print(min(path)+1)
    else:
        print(-1)