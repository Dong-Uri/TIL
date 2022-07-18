T = int(input())
Ns = []
Ms = []
As = []
Bs = []
for _ in range(T):
    N, M = map(int, input().split())
    Ns.append(N)
    Ms.append(M)
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    As.append(A)
    Bs.append(B)

ans = 'empty'
for i in range(T):
    ans = 0
    if Ns[i] <= Ms[i] :
        for j in range(Ms[i]-Ns[i]+1):
            hap = 0
            for k in range(Ns[i]):
                hap += As[i][k] * Bs[i][k+j]
            if (ans == 'empty') or (ans < hap):
                ans = hap
    if Ns[i] > Ms[i] :
        for j in range(Ns[i]-Ms[i]+1):
            hap = 0
            for k in range(Ms[i]):
                hap += Bs[i][k] * As[i][k+j]
            if (ans == 'empty') or (ans < hap):
                ans = hap
    print('#%d %d'%((i+1), ans))