T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = [0]
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[j][i] > 0:
                cnt += 1
            if arr[j][i] == 0 and cnt != 0:
                for k in range(ans[0]):
                    if ans[2*k+1] == cnt:
                        ans[2*k+2] += 1
                        break
                else: # for에 대한 else == break시 실행되지 않음
                    ans += [cnt, 1]
                    ans[0] += 1
                cnt = 0

    # ans 정렬
    if ans[0] != 0:
        for i in range(ans[0]-1):
            mins_i = 2*i+1
            for j in range(i+1, ans[0]):
                if ans[2*j+1] * ans[2*j+2] < ans[mins_i] * ans[mins_i+1] or (ans[2*j+1] * ans[2*j+2] == ans[mins_i] * ans[mins_i+1] and ans[2*j+1] < ans[mins_i]):
                    mins_i = 2*j+1
            ans[2*i+1], ans[2*i+2], ans[mins_i], ans[mins_i+1] = ans[mins_i], ans[mins_i+1], ans[2*i+1], ans[2*i+2]

    print(f'#{t}', *ans)