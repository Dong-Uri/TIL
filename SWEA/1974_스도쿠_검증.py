T = int(input())
checkset = {1,2,3,4,5,6,7,8,9}
for t in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    ans = 1
    for n in range(9):
        if set(sudoku[n]) != checkset:
            ans = 0
            break
        line = set()
        for m in range(9):
            line.add(sudoku[m][n])
        if set(line) != checkset:
            ans = 0
            break
    for n in range(3):
        if ans == 0:
            break
        for m in range(3):
            group = set()
            for i in range(3):
                for j in range(3):
                    group.add(sudoku[3*n+i][3*m+j])
            if set(group) != checkset:
                ans = 0
                break
    print(f'#{t} {ans}')