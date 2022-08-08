T = int(input())
ans_lst = []
for _ in range(T):
    N, S, E = map(int, input().split())
    M = int(input())
    A = []
    B = []
    for _ in range(M):
        u, v = map(int, input().split())
        A.append(u)
        B.append(v)
    stack = [S]
    count = 0
    ccount = None
    end = False
    while stack:
        if count != 0:
            ccount -= 1
            if ccount == 0:
                count += 1
                ccount = len(stack)
        now = stack.pop(0)
        if count == 0:
            for idx, a in enumerate(A):
                if now % a == 0:
                    A.pop(idx)
                    if E % B[idx] == 0:
                        ans_lst.append(count)
                        end = True
                        break
                    else:
                        stack.append(B[idx])
                        B.pop(idx)
            ccount = len(stack)
            count += 1
        else:
            for idx, a in enumerate(A):
                for i in range(max(a,now),(a*now)+1):
                    if i % a == 0 and i % now == 0:
                        minx = i
                        break
                if minx <= N:
                    A.pop(idx)
                    if E % B[idx] == 0:
                        ans_lst.append(count)
                        end = True
                        break
                    else:
                        stack.append(B[idx])
                        B.pop(idx)
        print(count, stack ,A, B, end, ccount)
        if end == True:
            break
    if end == False:
        ans_lst.append(-1)

for t in range(T):
    print(f'#{t+1} {ans_lst[t]}')