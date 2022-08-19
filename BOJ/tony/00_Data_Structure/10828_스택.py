import sys
N = int(input())
stk = []
for _ in range(N):
    order = sys.stdin.readline().rstrip()
    if order[:4] == 'push':
        stk.append(int(order[5:]))
    elif order == 'pop':
        if stk:
            print(stk.pop())
        else:
            print(-1)
    elif order == 'size':
        print(len(stk))
    elif order == 'empty':
        if stk:
            print(0)
        else:
            print(1)
    elif order == 'top':
        if stk:
            print(stk[-1])
        else:
            print(-1)
    else:
        pass