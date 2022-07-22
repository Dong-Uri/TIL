T = int(input())
answer = []
checkset = set([1,2,3,4,5,6,7,8,9])
for t in range(T):
    sudoku = []
    ans = 1
    for _ in range(9):
        line = [int(x) for x in input().split()]
        if set(line) != checkset:
            ans = 0
        sudoku.append(line)
    for n in range(9):
        yline = set()
        for m in range(9):
            yline.add(sudoku[m][n])
        if set(yline) != checkset:
            ans = 0
    for n in range(3):
        for m in range(3):
            group = set()
            for i in range(3):
                for j in range(3):
                    group.add(sudoku[3*n+i][3*m+j])
            if set(group) != checkset:
                ans = 0
    answer.append(ans)
for t in range(T):
    print('#%d %s'%((t+1), answer[t]))