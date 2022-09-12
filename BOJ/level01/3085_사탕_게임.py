N = int(input())
board = ['X' * (N+2)] + ['X' + input() + 'X' for _ in range(N)] + ['X' * (N+2)]
max_c = 0
for i in range(1, N+1):
    for j in range(1, N+1):

        # i,j 에서 오른쪽으로 검사
        candy = board[i][j]
        n = 1
        change = True
        for k in range(1, N - j + 1):
            if board[i][j + k] == candy:
                n += 1
            elif change and (board[i + 1][j + k] == candy or board[i - 1][j + k] == candy):
                n += 1
                change = False
            elif change and board[i][j + k + 1] == candy:
                n += 1
                break
            else:
                break
        if n > max_c:
            max_c = n

        # j, i에서 아래쪽으로 검사
        candy = board[j][i]
        n = 1
        change = True
        for k in range(1, N - j + 1):
            if board[j + k][i] == candy:
                n += 1
            elif change and (board[j + k][i + 1] == candy or board[j + k][i - 1] == candy):
                n += 1
                change = False
            elif change and board[j + k + 1][i] == candy:
                n += 1
                break
            else:
                break
        if n > max_c:
            max_c = n

        # 뒤쪽에서 부터 검사
        back_i = N - i + 1
        back_j = N - j + 1

        # back_i, back_j에서 왼쪽으로 검사
        candy = board[back_i][back_j]
        n = 1
        change = True
        for k in range(1, N - j + 1):
            if board[back_i][back_j - k] == candy:
                n += 1
            elif change and (board[back_i + 1][back_j - k] == candy or board[back_i - 1][back_j - k] == candy):
                n += 1
                change = False
            elif change and board[back_i][back_j - k - 1] == candy:
                n += 1
                break
            else:
                break
        if n > max_c:
            max_c = n

        # back_j, back_i에서 위쪽으로 검사
        candy = board[back_j][back_i]
        n = 1
        change = True
        for k in range(1, N - j + 1):
            if board[back_j - k][back_i] == candy:
                n += 1
            elif change and (board[back_j - k][back_i + 1] == candy or board[back_j - k][back_i - 1] == candy):
                n += 1
                change = False
            elif change and board[back_j - k - 1][back_i] == candy:
                n += 1
                break
            else:
                break
        if n > max_c:
            max_c = n
            
print(max_c)