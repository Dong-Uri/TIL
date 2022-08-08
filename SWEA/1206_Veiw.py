for t in range(1, 11):
    T = int(input())
    building_list = list(map(int, input().split()))
    jomang = 0 # 조망권 확보 세대 수
    for i in range(2,T-2): # 맨 왼쪽 두 칸과 맨 오른쪽 두 칸을 제외한 레인지
        near_max = max(building_list[i-2], building_list[i-1], building_list[i+1], building_list[i+2])
        # 양쪽으로 2칸 안에 있는 네 빌딩 중 가장 높은 빌딩
        if building_list[i] > near_max: # 양쪽의 네 빌딩보다 자신이 높다면
            jomang += building_list[i] - near_max # 조망권이 확보된 세대 수 추가 
    print(f'#{t} {jomang}')