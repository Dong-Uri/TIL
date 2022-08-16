white_paper = [[0]*100 for _ in range(100)]
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            white_paper[i][j] = 1
ans = 0
for i in range(100):
    for j in range(100):
        ans += white_paper[i][j]
print(ans)