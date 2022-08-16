N = int(input())
lst = list(map(int, input().split()))
last_n = up_cnt = down_cnt = ans = 0
for n in lst:
    
    # 숫자가 커지면 업카운트 증가 다운카운트 초기화
    if n > last_n:
        if down_cnt > ans:
            ans = down_cnt
        up_cnt += 1
        down_cnt = 1
        
    # 숫자가 작아지면 업카운트 초기화 다운카운트 증가
    elif n < last_n:
        if up_cnt > ans:
            ans = up_cnt
        up_cnt = 1
        down_cnt += 1
        
    # 숫자가 같으면 두 카운트 모두 증가
    else:
        up_cnt += 1
        down_cnt += 1
    last_n = n
    
# 마지막으로 카운트가 최대값인지 한번 더 확인
if down_cnt > ans:
    ans = down_cnt
if up_cnt > ans:
    ans = up_cnt
    
print(ans)