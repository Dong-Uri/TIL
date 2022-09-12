bingo_pan = [list(map(int, input().split())) for _ in range(5)]
call = []
for _ in range(5):
    call += list(map(int, input().split()))
cnt = 0
ans = 0
while ans == 0:

    # 빙고판에서 부른 값을 0으로 바꿈
    for i in range(5):
        for j in range(5):
            if bingo_pan[i][j] == call[cnt]:
                bingo_pan[i][j] = 0
                call[cnt] = 0
                break
        if call[cnt] == 0:
            break
            
    # 빙고 확인
    if cnt >= 11: # 12번 이후에 빙고가 생성될 수 있으므로
        bingo_cnt = 0
        bingo_c1 = bingo_c2 = True
        for i in range(5):
            bingo_x = bingo_y = True
            for j in range(5):
                if bingo_pan[i][j] > 0:
                    bingo_x = False
                if bingo_pan[j][i] > 0:
                    bingo_y = False
            if bingo_x:
                bingo_cnt += 1
            if bingo_y:
                bingo_cnt += 1
            if bingo_pan[i][i] > 0:
                bingo_c1 = False
            if bingo_pan[i][4-i] > 0:
                bingo_c2 = False
        if bingo_c1:
            bingo_cnt += 1
        if bingo_c2:
            bingo_cnt += 1
        
        # 빙고 3개 이상
        if bingo_cnt >= 3:
            ans = cnt + 1
    cnt += 1
print(ans)