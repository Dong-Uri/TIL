import sys
T = int(input())
for _ in range(T):
    PS = sys.stdin.readline().rstrip()
    stk = 0
    for gh in PS:
        if gh == '(':
            stk += 1
        else:
            stk -= 1
        if stk < 0:
            print('NO')
            break
    else:
        if stk > 0:
            print('NO')
        else:
            print('YES')