N = int(input())
pick_num = list(map(int, input().split()))
ans = []
for i in range(N):
    ans = ans[:i-pick_num[i]] + [i+1] + ans[i-pick_num[i]:]
print(*ans)