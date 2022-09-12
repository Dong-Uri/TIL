for _ in range(10):
    t = input()
    array100 = []
    for _ in range(100):
        arr = list(map(int, input().split()))
        array100.append(arr) # array100을 이중 list로 만듦
    max_hap = 0 # 최대값은 계산할때마다 체크하며 업데이트될 예정
    for i in range(100):
        hap_x = 0
        hap_y = 0
        for j in range(100):
            hap_x += array100[i][j] # i행의 모든 합 (x축)
            hap_y += array100[j][i] # i열의 모든 합 (y축)
        # 현재 최대값보다 높은 합이 있는 지 확인
        if hap_x > max_hap:
            max_hap = hap_x
        if hap_y > max_hap:
            max_hap = hap_y
    hap_cross1 = 0
    hap_cross2 = 0
    for c in range(100):
        hap_cross1 += array100[c][c] # 첫번째 대각선 합
        hap_cross2 += array100[c][99-c] # 두번째 대각선 합
    # 현재 최대값보다 높은 합이 있는 지 확인
    if hap_cross1 > max_hap:
        max_hap = hap_cross1
    if hap_cross2 > max_hap:
        max_hap = hap_cross2
    print(f'#{t} {max_hap}')