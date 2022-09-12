wood = list(map(int, input().split()))
ans = [1, 2, 3, 4, 5]
i = 0
while wood != ans:
    
    # 위치 바꿈
    if wood[i] > wood[i+1]:
        wood[i], wood[i+1] = wood[i+1], wood[i]
        print(*wood)
        
    # i값 증가
    i += 1
    
    # 1단계로 돌아가기
    if i == 4:
        i = 0