T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    reports = list(map(int, input().split()))
    ans = []
    for n in range(1, N+1):
        if n not in reports:
            ans += [n]
    print(f'#{t}', *ans)