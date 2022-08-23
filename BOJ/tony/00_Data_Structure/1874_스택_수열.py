n = int(input())
nums = [i for i in range(n, 0, -1)]
stk = []
ans = []
try:
    for _ in range(n):
        tg_num = int(input())

        # 처음 스택이 비었을때 push
        if not stk:
            stk.append(nums.pop())
            ans.append('+')

        # 스택의 top이 목표한 숫자일때까지 push
        while stk[-1] != tg_num:
            stk.append(nums.pop())
            ans.append('+')

        # 스택의 top이 목표한 숫자일때 pop
        if stk[-1] == tg_num:
            stk.pop()
            ans.append('-')

    for i in ans:
        print(i)

# 예외시 NO 출력
except:
    print('NO')