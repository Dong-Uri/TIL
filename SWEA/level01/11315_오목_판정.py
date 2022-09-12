def f():
    for i in range(N):

        # 가로 오목 찾기
        j = 0
        while j < N:
            for k in range(5):
                if j + k == N:
                    j = N
                    break
                if omok[i][j + k] != 'o':
                    j += k + 1
                    break
            else:
                return 'YES'

        # 세로 오목 찾기
        j = 0
        while j < N:
            for k in range(5):
                if j + k == N:
                    j = N
                    break
                if omok[j + k][i] != 'o':
                    j += k + 1
                    break
            else:
                return 'YES'

    # 대각선 오목 찾기
    for i in range(N - 4):
        for j in range(N - 4):
            for k in range(5):
                if omok[i + k][j + k] != 'o':
                    break
            else:
                return 'YES'
            for k in range(5):
                if omok[i + k][N - j - 1 - k] != 'o':
                    break
            else:
                return 'YES'

    # 위에서 오목을 못찾은 경우
    return 'NO'


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    omok = [input() for _ in range(N)]
    print(f'#{t} {f()}')