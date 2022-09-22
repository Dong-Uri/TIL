# 사각형 모양의 카페 경로를 찾는 함수
def find_sq(dia, i_s, i_e, j_s, j_e):

    # 경로 내에 0이 있다면 지역을 벗어났으므로 리턴으로 나옴
    for i in range(i_s, i_e + 1):
        if dia[i][j_s] == 0:
            return 0
        if dia[i][j_e] == 0:
            return 0
    for j in range(j_s, j_e + 1):
        if dia[i_s][j] == 0:
            return 0
        if dia[i_e][j] == 0:
            return 0

    # 우선 사각형의 네 모서리의 종류가 중복되는지 cafe 리스트를 만들며 확인
    cafe = [dia[i_s][j_s]]
    if dia[i_s][j_e] in cafe:
        return 0
    else:
        cafe.append(dia[i_s][j_e])
    if dia[i_e][j_s] in cafe:
        return 0
    else:
        cafe.append(dia[i_e][j_s])
    if dia[i_e][j_e] in cafe:
        return 0
    else:
        cafe.append(dia[i_e][j_e])

    # 모서리를 제외한 각 변의 종류가 중복되는지 cafe 리스트를 만들며 확인
    for i in range(i_s + 1, i_e):
        if dia[i][j_s] in cafe:
            return 0
        else:
            cafe.append(dia[i][j_s])
        if dia[i][j_e] in cafe:
            return 0
        else:
            cafe.append(dia[i][j_e])
    for j in range(j_s + 1, j_e):
        if dia[i_s][j] in cafe:
            return 0
        else:
            cafe.append(dia[i_s][j])
        if dia[i_e][j] in cafe:
            return 0
        else:
            cafe.append(dia[i_e][j])

    # 카페의 개수가 최대값이라면 최대값을 업데이트
    global max_cafe
    if len(cafe) > max_cafe:
        max_cafe = len(cafe)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    NxN = [list(map(int, input().split())) for _ in range(N)]

    # N이 홀수인 경우와 짝수인 경우로 나누어 대각선을 핀 두 2차원 배열을 만듦
    if N % 2:
        dia1 = [[0] * (N-2) for _ in range(N-2)]
        dia2 = [[0] * (N-1) for _ in range(N-1)]
        for i in range(N):
            for j in range(N):
                if (i == 0 or i == N-1) and (j == 0 or j == N-1):
                    continue
                elif (i + j) % 2:
                    dia2[(i+j-1)//2][(i-j+N-1)//2] = NxN[i][j]
                else:
                    dia1[(i+j-2)//2][(i-j+N-2)//2] = NxN[i][j]
    else:
        dia1 = [[0] * (N-1) for _ in range(N-2)]
        dia2 = [[0] * (N-1) for _ in range(N-2)]
        for i in range(N):
            for j in range(N):
                if (i == 0 or i == N-1) and (j == 0 or j == N-1):
                    continue
                elif (i + j) % 2:
                    dia2[(i-j+N-3)//2][(i+j-1)//2] = NxN[i][j]
                else:
                    dia1[(i+j-2)//2][(i-j+N-2)//2] = NxN[i][j]

    max_cafe = -1
    
    # 두 대각 2차원 배열에서 만들 수 있는 사각형의 모서리 값들
    for dia in (dia1, dia2):
        for i_s in range(len(dia) - 1):
            for i_e in range(len(dia) - 1, i_s, -1):
                for j_s in range(len(dia[0]) - 1):
                    for j_e in range(len(dia[0]) - 1, j_s, -1):
                        
                        # 해당 사각형이 최대값이 될수 있는 경우만 조사
                        if (i_e - i_s + j_e - j_s) * 2 > max_cafe:
                            find_sq(dia, i_s, i_e, j_s, j_e)
                            
    print(f'#{t} {max_cafe}')