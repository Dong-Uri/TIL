T = int(input())
for t in range(1, T+1):
    N = int(input())
    ans = []
    ans += [N // 50000]
    N = N % 50000
    ans += [N // 10000]
    N = N % 10000
    ans += [N // 5000]
    N = N % 5000
    ans += [N // 1000]
    N = N % 1000
    ans += [N // 500]
    N = N % 500
    ans += [N // 100]
    N = N % 100
    ans += [N // 50]
    N = N % 50
    ans += [N // 10]
    print(f'#{t}')
    print(*ans)