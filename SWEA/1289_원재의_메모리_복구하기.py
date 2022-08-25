T = int(input())
for t in range(1, T+1):
    memory = input()
    s = '1' # 덮어씌울 값
    cnt = 0 # 고친 횟수
    for i in memory:
        
        # 덮어씌울 값이 나오면 고침
        if i == s:
            cnt += 1
            
            # 덮어씌울 값 변경
            if s == '1':
                s = '0'
            else:
                s = '1'
                
    print(f'#{t} {cnt}')