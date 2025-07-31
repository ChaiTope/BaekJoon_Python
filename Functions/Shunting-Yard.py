def infix_to_postfix(expr):
    # 연산자 우선순위 정의
    prec = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '^' : 3}
    output = []
    stack = []

    tokens = list(expr)  # 한 글자씩 토큰화 (필요에 따라 다중 자리 수 처리 추가)
    for tok in tokens:
        if tok.isalnum():  # 숫자나 문자 (피연산자)
            output.append(tok)
        elif tok == '(':
            stack.append(tok)
        elif tok == ')':
            # '(' 나올 때까지 스택 비우기
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # '(' 버리기
        else:
            # 연산자 처리
            # 왼쪽 결합(L)이라 가정 (^(지수)는 보통 오른쪽 결합)
            while stack and stack[-1] != '(' and (
                (prec[stack[-1]] > prec[tok]) or
                (prec[stack[-1]] == prec[tok] and tok != '^')
            ):
                output.append(stack.pop())
            stack.append(tok)

    # 남은 연산자 전부 출력
    while stack:
        output.append(stack.pop())

    return ''.join(output)

# 예시
expr = "A*(B+C)/D"
print(infix_to_postfix(expr))  # → "ABC+*D/"
