def gh(gualho):
    for i in gualho:
        num = 0
        if i == ')':
            while True:
                if not stk: # 옳지 않은 괄호열 1
                    return 0
                top = stk.pop()
                if top == '(':
                    # () 안의 수들의 합 * 2
                    if num:
                        num *= 2
                    # () 안에 수가 없으면 2
                    else:
                        num = 2
                    stk.append(num)
                    break
                elif top == '[': # 옳지 않은 괄호열 2
                    return 0
                # () 안의 수들을 더함
                else:
                    num += top
        elif i == ']':
            while True:
                if not stk: # 옳지 않은 괄호열 3
                    return 0
                top = stk.pop()
                if top == '[':
                    # [] 안의 수들의 합 * 3
                    if num:
                        num *= 3
                    # [] 안에 수가 없으면 3
                    else:
                        num = 3
                    stk.append(num)
                    break
                elif top == '(': # 옳지 않은 괄호열 4
                    return 0
                # [] 안의 수들을 더함
                else:
                    num += top
        else:
            stk.append(i)
    for i in stk:
        if i == '(' or i == '[': # 옳지 않은 괄호열 5
            return 0
    return sum(stk)

gualho = input()
stk = []
print(gh(gualho))