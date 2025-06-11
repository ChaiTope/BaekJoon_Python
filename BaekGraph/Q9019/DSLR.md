# Gold 4

## 문제
네 개의 명령어 D, S, L, R 을 이용하는 간단한 계산기가 있다. 이 계산기에는 레지스터가 하나 있는데, 이 레지스터에는 0 이상 10,000 미만의 십진수를 저장할 수 있다. 각 명령어는 이 레지스터에 저장된 n을 다음과 같이 변환한다. n의 네 자릿수를 d1, d2, d3, d4라고 하자(즉 n = ((d1 × 10 + d2) × 10 + d3) × 10 + d4라고 하자)

    D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다. 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
    S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. n이 0 이라면 9999 가 대신 레지스터에 저장된다.
    L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
    R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.
위에서 언급한 것처럼, L 과 R 명령어는 십진 자릿수를 가정하고 연산을 수행한다. 예를 들어서 n = 1234 라면 여기에 L 을 적용하면 2341 이 되고 R 을 적용하면 4123 이 된다.

여러분이 작성할 프로그램은 주어진 서로 다른 두 정수 A와 B(A ≠ B)에 대하여 A를 B로 바꾸는 최소한의 명령어를 생성하는 프로그램이다. 예를 들어서 A = 1234, B = 3412 라면 다음과 같이 두 개의 명령어를 적용하면 A를 B로 변환할 수 있다.

1234 →L 2341 →L 3412
1234 →R 4123 →R 3412

따라서 여러분의 프로그램은 이 경우에 LL 이나 RR 을 출력해야 한다.

n의 자릿수로 0 이 포함된 경우에 주의해야 한다. 예를 들어서 1000 에 L 을 적용하면 0001 이 되므로 결과는 1 이 된다. 그러나 R 을 적용하면 0100 이 되므로 결과는 100 이 된다.

## 입력
프로그램 입력은 T 개의 테스트 케이스로 구성된다. 테스트 케이스 개수 T 는 입력의 첫 줄에 주어진다. 각 테스트 케이스로는 두 개의 정수 A와 B(A ≠ B)가 공백으로 분리되어 차례로 주어지는데 A는 레지스터의 초기 값을 나타내고 B는 최종 값을 나타낸다. A 와 B는 모두 0 이상 10,000 미만이다.

## 출력
A에서 B로 변환하기 위해 필요한 최소한의 명령어 나열을 출력한다. 가능한 명령어 나열이 여러가지면, 아무거나 출력한다.

## Thinking!!

## 함수 호출 처리(시간초과)
    from collections import deque
    import sys
    
    input = sys.stdin.readline
    
    T = int(input())
    
    def D(n):
        return (n * 2) % 10000
    
    def S(n):
        if n == 0:
            return 9999
        else:
            return n - 1
    
    def L(n):
        return (n % 1000) * 10 + (n // 1000)
    
    def R(n):
        return (n % 10) * 1000 + (n // 10)
    
    for _ in range(T):
        A, B = map(int, input().split())
        visited = [False]*10000
        parent = [-1]*10000        # parent[x] = x로 오기 전 숫자
        how = ['']*10000           # how[x]   = parent[x] -> x 로 사용된 명령어
    
        q = deque([A])
        visited[A] = True
    
        while q:
            cur = q.popleft()
            if cur == B:
                break
            for op, ch in [(D,'D'), (S,'S'), (L,'L'), (R,'R')]:
                nxt = op(cur)
                if not visited[nxt]:
                    visited[nxt] = True
                    parent[nxt] = cur
                    how[nxt] = ch
                    q.append(nxt)
    
        # 역추적: B → A 로 올라가면서 how[] 수집
        res = []
        x = B
        while x != A:
            res.append(how[x])
            x = parent[x]
        print(''.join(reversed(res)))

함수로 만들어서 해봤는데, 파이썬 내에서 함수 불러오고 하는데
시간이 오래걸려서 시간초과가 나는 것 같다.

리스트 인덱싱으로 처리해야 할 거 같다.

## 그냥 python이라 느렸던것

    from collections import deque
    import sys
    
    input = sys.stdin.readline
    
    T = int(input())
    
    def D(n):
        return (n * 2) % 10000
    
    def S(n):
        if n == 0:
            return 9999
        else:
            return n - 1
    
    def L(n):
        return (n % 1000) * 10 + (n // 1000)
    
    def R(n):
        return (n % 10) * 1000 + (n // 10)
    
    for _ in range(T):
        A, B = map(int, input().split())
        visited = [False]*10000
        parent = [-1]*10000        # parent[x] = x로 오기 전 숫자
        how = ['']*10000           # how[x]   = parent[x] -> x 로 사용된 명령어
    
        q = deque([A])
        visited[A] = True
    
        while q:
            cur = q.popleft()
            if cur == B:
                break
            for op, ch in [(D,'D'), (S,'S'), (L,'L'), (R,'R')]:
                nxt = op(cur)
                if not visited[nxt]:
                    visited[nxt] = True
                    parent[nxt] = cur
                    how[nxt] = ch
                    q.append(nxt)
    
        # 역추적: B → A 로 올라가면서 how[] 수집
        res = []
        x = B
        while x != A:
            res.append(how[x])
            x = parent[x]
        print(''.join(reversed(res)))

pypy3으로 바꾸니까, 함수 내 연산을 문자열 연산에서 산술연산으로 바꾼 시점에서 통과되는 것을 알았다.
그냥 python이 느려서 통과가 안되는 것 같다. 채점기록에도 pypy3만 있고 python은 한개도 없어