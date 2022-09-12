for t in range(1, 11):
    _ = input()
    gualho = input()
    stk = []
    ans = 1
    for i in gualho:

        # 여는 괄호는 스택에 추가
        if i == '(' or i == '[' or i == '{' or i == '<':
            stk.append(i)

        # 닫는 괄호일 때는 스택의 top과 괄호가 일치하는지 확인후 제거
        elif i == ')' and stk and stk[-1] == '(':
            stk.pop()
        elif i == ']' and stk and stk[-1] == '[':
            stk.pop()
        elif i == '}' and stk and stk[-1] == '{':
            stk.pop()
        elif i == '>' and stk and stk[-1] == '<':
            stk.pop()

        # 그 외의 경우 유효하지 않음
        else:
            ans = 0
            break
    
    # 스택이 남아있는 경우도 유효하지 않음
    if stk:
        ans = 0

    print(f'#{t} {ans}')