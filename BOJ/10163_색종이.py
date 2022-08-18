N = int(input())
grid = [[0] * 1001 for _ in range(1001)]

# n번 색종이가 놓이는 곳에 n을 입력
for n in range(1, N+1):
    x, y, w, h = map(int, input().split())
    for i in range(x, x+w):
        grid[i][y:y+h] = [n] * h

# n이 입력된 면적을 출력
for n in range(1, N+1):
    ans = 0
    for i in range(1001):
        ans += grid[i].count(n)
    print(ans)