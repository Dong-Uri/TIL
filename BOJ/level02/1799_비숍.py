import copy

def bishop(pan, i, n):
    global ans
    if i == len(pan):
        if n > ans:
            ans = n
        return
    nothing = True
    for j in range(len(pan[0])):
        if pan[i][j]:
            new_pan = copy.deepcopy(pan)
            for next_i in range(i+1, len(pan)):
                new_pan[next_i][j] = 0
            bishop(new_pan, i+1, n+1)
            nothing = False
    if nothing:
        bishop(pan, i+1, n)
    return

N = int(input())
chess = []
answer = 0
for _ in range(N):
    line = list(map(int, input().split()))
    chess.append(line)
if N % 2:
    chess_1 = [[0] * N for _ in range(N)]
    chess_2 = [[0] * (N-1) for _ in range(N-1)]
    for i in range(N):
        for j in range(N):
            if (i + j) % 2:
                chess_2[(i - j + N - 1) // 2][(i + j - 1) // 2] = chess[i][j]
            else:
                chess_1[(i - j + N) // 2][(i + j) // 2] = chess[i][j]
else:
    chess_1 = [[0] * N for _ in range(N-1)]
    chess_2 = [[0] * (N-1) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if (i + j) % 2:
                chess_2[(i - j + N) // 2][(i + j - 1) // 2] = chess[i][j]
            else:
                chess_1[(i - j + N - 1) // 2][(i + j) // 2] = chess[i][j]

answer = 0
ans = 0
bishop(chess_1, 0, 0)
answer += ans
ans = 0
bishop(chess_2, 0, 0)
answer += ans
print(answer)