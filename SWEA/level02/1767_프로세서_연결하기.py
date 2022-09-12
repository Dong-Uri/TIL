import copy

# 각각의 코어의 연결을 체크하는 함수
# 재귀로 모든 코어를 돕니다.
def f(a, length, connect, line, mxns):
    global connect_max
    global line_min

    # 앞으로 모든 코어를 연결해도 최대 연결 수에 도달하지 못하는 경우는 탐색 중지
    if connect + length - a < connect_max:
        return

    # 모든 코어를 탐색했을때 연결 수와 라인의 길이를 비교하여 답을 저장
    if a == length:
        if connect > connect_max:
            connect_max = connect
            line_min = line
        elif connect == connect_max and line < line_min:
            line_min = line
        return

    # 다음 4가지 재귀함수로 갈 변수들이 각각 다르게 변하므로 복사해서 사용
    connect1 = connect2 = connect3 = connect4 = connect
    line1 = line2 = line3 = line4 = line
    mxns1 = copy.deepcopy(mxns)
    mxns2 = copy.deepcopy(mxns)
    mxns3 = copy.deepcopy(mxns)
    mxns4 = copy.deepcopy(mxns)

    # 코어를 아래로 연결할 때
    i = 1
    # 연결이 가능한지 확인
    while core[a][0] + i <= N-1:
        if mxns[core[a][0] + i][core[a][1]] != 0:
            break
        i += 1
    # 연결이 가능하다면 연결한 후 다음 코어로 재귀
    else:
        i = 1
        connect1 += 1
        while core[a][0] + i <= N - 1:
            mxns1[core[a][0] + i][core[a][1]] = 2
            line1 += 1
            i += 1
    f(a+1, length, connect1, line1, mxns1)

    # 코어를 위로 연결할 때
    i = 1
    # 연결이 가능한지 확인
    while core[a][0] - i >= 0:
        if mxns[core[a][0] - i][core[a][1]] != 0:
            break
        i += 1
    # 연결이 가능하다면 연결한 후 다음 코어로 재귀
    else:
        i = 1
        connect2 += 1
        while core[a][0] - i >= 0:
            mxns2[core[a][0] - i][core[a][1]] = 2
            line2 += 1
            i += 1
    f(a + 1, length, connect2, line2, mxns2)

    # 코어를 오른쪽으로 연결할 때
    i = 1
    # 연결이 가능한지 확인
    while core[a][1] + i <= N - 1:
        if mxns[core[a][0]][core[a][1] + i] != 0:
            break
        i += 1
    # 연결이 가능하다면 연결한 후 다음 코어로 재귀
    else:
        i = 1
        connect3 += 1
        while core[a][1] + i <= N - 1:
            mxns3[core[a][0]][core[a][1] + i] = 2
            line3 += 1
            i += 1
    f(a + 1, length, connect3, line3, mxns3)

    # 코어를 왼쪽으로 연결할 때
    i = 1
    # 연결이 가능한지 확인
    while core[a][1] - i >= 0:
        if mxns[core[a][0]][core[a][1] - i] != 0:
            break
        i += 1
    # 연결이 가능하다면 연결한 후 다음 코어로 재귀
    else:
        i = 1
        connect4 += 1
        while core[a][1] - i >= 0:
            mxns4[core[a][0]][core[a][1] - i] = 2
            line4 += 1
            i += 1
    f(a + 1, length, connect4, line4, mxns4)

T = int(input())
for t in range(1, T+1):
    N = int(input())

    # NxN 그리드와 모서리에 접하지 않은 코어들의 리스트를 저장
    NxN = []
    core = []
    for i in range(N):
        lst = list(map(int, input().split()))
        for j in range(N):
            if i != 0 and j != 0 and i != N-1 and j != N-1 and lst[j] == 1:
                core.append([i, j])
        NxN.append(lst)
    
    connect_max = -1
    line_min = 144
    f(0, len(core), 0, 0, NxN)
    print(f'#{t} {line_min}')