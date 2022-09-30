T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for t in range(1, T+1):
    N = int(input())
    atom = []
    power = [0] * N
    for n in range(N):
        x, y, m, K = map(int, input().split())
        atom.append([x, y, m, n])   # 에너지 대신 번호를 추가 (중복이 없도록)
        power[n] = K                # 에너지는 따로 리스트 저장

    # 모든 두 원자가 충돌하는 경우를 확인하여 impact[시간*2]안에 리스트로 저장
    impact = [[] for _ in range(4001)]
    for i in range(N):
        for j in range(i + 1, N):

            # 두 원자가 같은 x에 있는 경우
            if atom[i][0] == atom[j][0]:
                if atom[i][1] < atom[j][1] and atom[i][2] == 0 and atom[j][2] == 1:
                    impact[atom[j][1] - atom[i][1]].append([atom[i][3], atom[j][3]])
                elif atom[i][1] > atom[j][1] and atom[i][2] == 1 and atom[j][2] == 0:
                    impact[atom[i][1] - atom[j][1]].append([atom[i][3], atom[j][3]])

            # 두 원자가 같은 y에 있는 경우
            elif atom[i][1] == atom[j][1]:
                if atom[i][0] < atom[j][0] and atom[i][2] == 3 and atom[j][2] == 2:
                    impact[atom[j][0] - atom[i][0]].append([atom[i][3], atom[j][3]])
                elif atom[i][0] > atom[j][0] and atom[i][2] == 2 and atom[j][2] == 3:
                    impact[atom[i][0] - atom[j][0]].append([atom[i][3], atom[j][3]])

            # 두 원자의 같은 대각선에 있는 경우1 (x+y가 같은 경우)
            elif atom[i][0] + atom[i][1] == atom[j][0] + atom[j][1]:
                if atom[i][0] < atom[j][0] and (atom[i][2] == 1 and atom[j][2] == 2 or atom[i][2] == 3 and atom[j][2] == 0):
                    impact[(atom[j][0] - atom[i][0]) * 2].append([atom[i][3], atom[j][3]])
                elif atom[i][0] > atom[j][0] and (atom[i][2] == 2 and atom[j][2] == 1 or atom[i][2] == 0 and atom[j][2] == 3):
                    impact[(atom[i][0] - atom[j][0]) * 2].append([atom[i][3], atom[j][3]])

            # 두 원자의 같은 대각선에 있는 경우2 (x-y가 같은 경우)
            elif atom[i][0] - atom[i][1] == atom[j][0] - atom[j][1]:
                if atom[i][0] < atom[j][0] and (atom[i][2] == 0 and atom[j][2] == 2 or atom[i][2] == 3 and atom[j][2] == 1):
                    impact[(atom[j][0] - atom[i][0]) * 2].append([atom[i][3], atom[j][3]])
                elif atom[i][0] > atom[j][0] and (atom[i][2] == 2 and atom[j][2] == 0 or atom[i][2] == 1 and atom[j][2] == 3):
                    impact[(atom[i][0] - atom[j][0]) * 2].append([atom[i][3], atom[j][3]])

    # 시간이 빠른 경우부터 충돌을 처리하고 얻는 에너지를 더함
    explode = [-1] * N
    ans = 0
    for n in range(4001):
        for c in impact[n]:

            # 두 원자가 아직 충돌하지 않은 경우
            if explode[c[0]] == -1 and explode[c[1]] == -1:
                explode[c[0]] = explode[c[1]] = n
                ans += power[c[0]] + power[c[1]]

            # 두 원자 중 하나가 같은 시간에 충돌한 경우 (3, 4개의 원자가 같이 충돌하는 경우)
            elif explode[c[0]] == n and explode[c[1]] == -1:
                explode[c[1]] = n
                ans += power[c[1]]
            elif explode[c[0]] == -1 and explode[c[1]] == n:
                explode[c[0]] = n
                ans += power[c[0]]
                
    print(f'#{t} {ans}')