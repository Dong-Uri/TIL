T = int(input())
answer = []
for t in range(T):
    N, K = map(int, input().split())
    NxN = []
    for _ in range(N):
        Nx = [int(x) for x in input().split()]
        NxN.append(Nx)
    test = [0]
    for _ in range(K):
        test.append(1)
    test.append(0)
    ans = 0
    for n in range(N):
        test_line = [0] + NxN[n] + [0]
        for i in range(N-K+1):
            if test == test_line[i:i+K+2]:
                ans += 1
        test_line = [0]
        for m in range(N):
            test_line.append(NxN[m][n])
        test_line.append(0)
        for i in range(N-K+1):
            if test == test_line[i:i+K+2]:
                ans += 1
    answer.append(ans)
for t in range(T):
    print('#%d %d'%((t+1), answer[t]))