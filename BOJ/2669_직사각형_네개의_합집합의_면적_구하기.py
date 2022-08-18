plane = [[0] * 100 for _ in range(100)]
for _ in range(4):
    # 입력 받은 내부를 0에서 1로
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            plane[x][y] = 1

# 1의 개수 == 넓이
ans = 0
for line in plane:
    for point in line:
        ans += point
        
print(ans)