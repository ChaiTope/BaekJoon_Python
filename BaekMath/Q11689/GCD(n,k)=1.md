# Gold 1

## 문제
자연수 n이 주어졌을 때, GCD(n, k) = 1을 만족하는 자연수 1 ≤ k ≤ n 의 개수를 구하는 프로그램을 작성하시오.

## 입력
첫째 줄에 자연수 n (1 ≤ n ≤ 1012)이 주어진다.

## 출력
GCD(n, k) = 1을 만족하는 자연수 1 ≤ k ≤ n 의 개수를 출력한다.

## Thinking!!
GCD구하기가 얼마 전이었던 것 같은데, 이번엔 역산인가?

논리

    입력: n
    result = n
    x = n
    
    for i from 2 to while i * i <= x:
        if x % i == 0:
            # i는 x의 소인수
            while x % i == 0:
                x //= i      # i를 몽땅 떼어냄
            result -= result // i   # result *= (1 - 1/i)
    
    # 루프 끝나고 x > 1이면, x 자체가 마지막 남은 소인수
    if x > 1:
        result -= result // x
    
    출력: result
i가 홀수일 때 만 탐색해도 가능

    i = 2
    while i * i <= x:
        if x % i == 0:
            while x % i == 0:
                x //= i
            result -= result // i
        i += 1 if i == 2 else 2   # 2 이후론 홀수만
