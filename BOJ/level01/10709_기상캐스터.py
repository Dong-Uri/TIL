H, W = map(int, input().split())
for _ in range(H):
    cloud = input()
    cast = -1 # 예보할 값
    ans = []
    for i in cloud:
        
        # 구름이 보이면 0으로 예보
        if i == 'c':
            cast = 0
        
        # 구름이 보인 이후로는 1씩 증가하며 예보
        elif cast != -1:
            cast += 1
            
        ans.append(cast)
    print(*ans)