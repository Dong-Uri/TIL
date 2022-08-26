sik = input()
stk = ['!']
hu = ''
for i in sik:

    # 문자열에 (가 나오면 스택에 push
    if i == '(':
        stk.append(i)

    # 문자열에 )가 나오면 괄호 안에 계산식들 추가
    elif i == ')':
        while True:
            if stk[-1] == '*':
                stk.pop()
                hu += '*'
            elif stk[-1] == '/':
                stk.pop()
                hu += '/'
            elif stk[-1] == '+':
                stk.pop()
                hu += '+'
            elif stk[-1] == '-':
                stk.pop()
                hu += '-'
            elif stk[-1] == '(':
                stk.pop()
                break

    # +와 -의 경우
    elif i == '+' or i == '-':
        while stk[-1] == '*' or stk[-1] == '/' or stk[-1] == '+' or stk[-1] == '-':
            hu += stk.pop()
        stk.append(i)

    # *와 /인 경우
    elif i == '*' or i == '/':
        while stk[-1] == '*' or stk[-1] == '/':
            hu += stk.pop()
        stk.append(i)

    # 알파벳은 바로 추가
    else:
        hu += i

# 문자열을 모두 돌았으므로 남은 스택의 계산식 해결
while stk[-1] != '!':
    if stk[-1] == '*':
        stk.pop()
        hu += '*'
    elif stk[-1] == '/':
        stk.pop()
        hu += '/'
    elif stk[-1] == '+':
        stk.pop()
        hu += '+'
    elif stk[-1] == '-':
        stk.pop()
        hu += '-'

print(hu)