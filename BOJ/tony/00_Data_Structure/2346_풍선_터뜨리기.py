N = int(input())
lst = list(map(int, input().split()))
num = [n for n in range(1, N+1)]
i = 0
ans = []
while True:
    
    # 풍선을 터트림
    move = lst.pop(i)
    
    # 터트린 풍선 번호 추가
    n = num.pop(i)
    ans.append(n)
    if not lst:
        break
    
    # pop한 값만큼 이동하여 다음 풍선 위치를 찾음
    N -= 1
    if move > 0:
        i = (i + move - 1) % N
    else:
        i = (i + move) % N
        
print(*ans)