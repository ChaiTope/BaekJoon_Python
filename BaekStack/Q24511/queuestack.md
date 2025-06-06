# Silver 3

## 문제
한가롭게 방학에 놀고 있던 도현이는 갑자기 재밌는 자료구조를 생각해냈다. 그 자료구조의 이름은 queuestack이다.

queuestack의 구조는 다음과 같다. 
$1$번, 
$2$번, ... , 
$N$번의 자료구조(queue 혹은 stack)가 나열되어있으며, 각각의 자료구조에는 한 개의 원소가 들어있다.

queuestack의 작동은 다음과 같다.

 
$x_0$을 입력받는다.
 
$x_0$을 
$1$번 자료구조에 삽입한 뒤 
$1$번 자료구조에서 원소를 pop한다. 그때 pop된 원소를 
$x_1$이라 한다.
 
$x_1$을 
$2$번 자료구조에 삽입한 뒤 
$2$번 자료구조에서 원소를 pop한다. 그때 pop된 원소를 
$x_2$이라 한다.
...
 
$x_{N-1}$을 
$N$번 자료구조에 삽입한 뒤 
$N$번 자료구조에서 원소를 pop한다. 그때 pop된 원소를 
$x_N$이라 한다.
 
$x_N$을 리턴한다.
도현이는 길이 
$M$의 수열 
$C$를 가져와서 수열의 원소를 앞에서부터 차례대로 queuestack에 삽입할 것이다. 이전에 삽입한 결과는 남아 있다. (예제 
$1$ 참고)

queuestack에 넣을 원소들이 주어졌을 때, 해당 원소를 넣은 리턴값을 출력하는 프로그램을 작성해보자.

## 입력
첫째 줄에 queuestack을 구성하는 자료구조의 개수 
$N$이 주어진다. (
$1 \leq N \leq 100\,000$)

둘째 줄에 길이 
$N$의 수열 
$A$가 주어진다. 
$i$번 자료구조가 큐라면 
$A_i = 0$, 스택이라면 
$A_i = 1$이다.

셋째 줄에 길이 
$N$의 수열 
$B$가 주어진다. 
$B_i$는 
$i$번 자료구조에 들어 있는 원소이다. (
$1 \leq B_i \leq 1\,000\,000\,000$)

넷째 줄에 삽입할 수열의 길이 
$M$이 주어진다. (
$1 \leq M \leq 100\,000$)

다섯째 줄에 queuestack에 삽입할 원소를 담고 있는 길이 
$M$의 수열 
$C$가 주어진다. (
$1 \leq C_i \leq 1\,000\,000\,000$)

입력으로 주어지는 모든 수는 정수이다.

## 출력
수열 
$C$의 원소를 차례대로 queuestack에 삽입했을 때의 리턴값을 공백으로 구분하여 출력한다.

## Thinking!!
아 그니까 a1 a2 a3 a4가 배열에 있고, 새 값 b1 b2 b3이 있다면 a2 a3가 스택이면 1회 실행시 b1 a2 a3 a1 ==> a4 나옴
2회차에 b2 a2 a3 b1 ==> a1나옴 3회차에 b3 a2 a3 b2 ==> b1나옴 이런식인가?

## 1차 시도
    import sys
    from collections import deque
    
    N = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline().strip())
    C = list(map(int, sys.stdin.readline().split()))
    
    que_count = 0
    queue_values = deque()
    for i in range(N):
        if A[i] == 0:
            queue_values.append(B[i])
            que_count += 1
    
    
    result = []
    
    if que_count > 0:
        C = reversed(C)
    
    for c in C:
        if queue_values:
            result.append(queue_values.pop())
        else:
            result.append(c)
    
    print(*result)
    
## 2차 시도
조부상때문에 일주일이 지나고 다시 풀어봤는데.
그냥 바로 풀린다. 뭐지 확실히 안되는날에는 안되는구나