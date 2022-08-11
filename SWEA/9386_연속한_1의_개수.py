T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input())) + [0]
    cnt = max_ones = 0
    for n in nums:
        if n == 1:
            cnt += 1
        else:
            if cnt > max_ones:
                max_ones = cnt
            cnt = 0
    print(f'#{t} {max_ones}')