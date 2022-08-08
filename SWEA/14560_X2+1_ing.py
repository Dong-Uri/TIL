T = int(input())
def X(a,b):
    return a+1, b*2
def Y(a,b):
    return a*2, b+1
ans_lst = []
for _ in range(T):
    oa, ob = map(int, input().split())
    stack = ['X', 'Y']
    while True:
        print(stack)
        a = oa
        b = ob
        cheak = stack.pop(0)
        for xy in cheak:
            if xy == 'X':
                a,b = X(a,b)
            elif xy == 'Y':
                a,b = Y(a,b)
        if a == b:
            ans_lst.append(cheak)
            break
        else:
            stack.append(cheak+'X')
            stack.append(cheak+'Y')
for t in range(T):
    print(f'#{t+1} {ans_lst[t]}')