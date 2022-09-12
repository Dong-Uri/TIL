N, K = map(int, input().split())
stu_cnt = [0] * 12
for _ in range(N):
    S, Y = map(int, input().split())
    stu_cnt[2 * Y - S - 1] += 1
ans = 0
for i in stu_cnt:
    ans += (i - 1) // K + 1
print(ans)