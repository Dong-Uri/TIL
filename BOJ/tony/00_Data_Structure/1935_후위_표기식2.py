N = int(input())
sik = input()

# 문자에 대한 수를 딕셔너리로 저장
dict = {}
for n in range(N):
    dict[chr(n + ord('A'))] = int(input())
    
stk = []
for i in sik:
    
    # 영대문자가 나오면 그에 대한 숫자를 스택에 push
    if i.isupper():
        stk.append(dict[i])
        
    # 수식이 나오면 pop을 통해 계산
    else:
        num2 = stk.pop()
        num1 = stk.pop()
        if i == '+':
            stk.append(num1 + num2)
        elif i == '-':
            stk.append(num1 - num2)
        elif i == '*':
            stk.append(num1 * num2)
        elif i == '/':
            stk.append(num1 / num2)
            
print(f'{stk[0]:.2f}')