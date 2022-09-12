for t in range(1, 11):
    _ = int(input())
    sik = input()
    stk = ['!']
    nums = []
    for i in sik:

        # 문자열에 숫자가 나오면 nums 리스트에 추가
        if i.isnumeric():
            nums.append(int(i))

        # 문자열에 (가 나오면 스택에 push
        elif i == '(':
            stk.append(i)

        # 문자열에 )가 나오면 괄호 안에 계산식들 해결
        elif i == ')':
            while True:
                if stk[-1] == '*':      # 곱셈
                    stk.pop()
                    nums.append(nums.pop() * nums.pop())
                elif stk[-1] == '+':    # 덧셈
                    stk.pop()
                    nums.append(nums.pop() + nums.pop())
                elif stk[-1] == '(':    # 괄호의 시작
                    stk.pop()
                    break

        # 문자열에 +가 나오면 +보다 우선인 계산식 해결
        elif i == '+':
            if stk[-1] == '*':
                stk.pop()
                nums.append(nums.pop() * nums.pop())
            if stk[-1] == '+':
                stk.pop()
                nums.append(nums.pop() + nums.pop())
            stk.append(i)

        # 문자열에 *가 나오면 *보다 우선인 계산식 해결
        elif i == '*':
            if stk[-1] == '*':
                stk.pop()
                nums.append(nums.pop() * nums.pop())
            stk.append(i)

    # 문자열을 모두 돌았으므로 남은 스택의 계산식 해결
    while stk[-1] != '!':
        if stk[-1] == '*':
            stk.pop()
            nums.append(nums.pop() * nums.pop())
        elif stk[-1] == '+':
            stk.pop()
            nums.append(nums.pop() + nums.pop())

    print(f'#{t} {nums[0]}')

# 하위 문제
# 1222_계산기1
# 1223_계산기2