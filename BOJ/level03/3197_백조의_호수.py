import copy

R, C = map(int, input().split())
lake = []
swan = []
for r in range(R):
    line = input()
    lake.append(list(line))
    for c in range(C):
        if line[c] == 'L':
            swan.append((r, c))
go = [(1, 0), (-1, 0), (0, 1), (0, -1)]
now = [swan[0]]
swan_1 = [swan[0]]
ans = 0
is_ans = False
while now:
    if is_ans:
        break
    r, c = now.pop()
    lake[r][c] = '1'
    for g_r, g_c in go:
        n_r = r + g_r
        n_c = c + g_c
        if 0 <= n_r < R and 0 <= n_c < C:
            if lake[n_r][n_c] == 'L':
                print(ans)
                is_ans = True
                break
            if lake[n_r][n_c] == '.':
                lake[n_r][n_c] = '1'
                now.append((n_r, n_c))
                swan_1.append((n_r, n_c))
now = [swan[1]]
swan_2 = [swan[1]]
while now:
    if is_ans:
        break
    r, c = now.pop()
    lake[r][c] = '2'
    for g_r, g_c in go:
        n_r = r + g_r
        n_c = c + g_c
        if 0 <= n_r < R and 0 <= n_c < C:
            if lake[n_r][n_c] == '.':
                lake[n_r][n_c] = '2'
                now.append((n_r, n_c))
                swan_2.append((n_r, n_c))
swan_n = []
if not is_ans:
    for r in range(R):
        for c in range(C):
            if lake[r][c] == '.':
                swan_n.append((r,c))
while not is_ans:
    ans += 1
    new_swan_n = []
    for r, c in swan_n:
        for g_r, g_c in go:
            n_r = r + g_r
            n_c = c + g_c
            if 0 <= n_r < R and 0 <= n_c < C:
                if lake[n_r][n_c] == 'X':
                    new_swan_n.append((n_r, n_c))
                    lake[n_r][n_c] = '.'
    new_swan_1 = []
    for r, c in swan_1:
        if is_ans:
            break
        for g_r, g_c in go:
            n_r = r + g_r
            n_c = c + g_c
            if 0 <= n_r < R and 0 <= n_c < C:
                if lake[n_r][n_c] == 'X' or lake[n_r][n_c] == '.':
                    new_swan_1.append((n_r, n_c))
                    lake[n_r][n_c] = '1'
    new_swan_2 = []
    for r, c in swan_2:
        if is_ans:
            break
        for g_r, g_c in go:
            n_r = r + g_r
            n_c = c + g_c
            if 0 <= n_r < R and 0 <= n_c < C:
                if lake[n_r][n_c] == 'X' or lake[n_r][n_c] == '.':
                    new_swan_2.append((n_r, n_c))
                    lake[n_r][n_c] = '2'
    new_new_swan_1 = copy.deepcopy(new_swan_1)
    while new_swan_1:
        if is_ans:
            break
        r, c = new_swan_1.pop()
        for g_r, g_c in go:
            n_r = r + g_r
            n_c = c + g_c
            if 0 <= n_r < R and 0 <= n_c < C:
                if lake[n_r][n_c] == '2':
                    is_ans = True
                    print(ans)
                    break
                if lake[n_r][n_c] == '.':
                    new_swan_1.append((n_r, n_c))
                    new_new_swan_1.append((n_r, n_c))
                    lake[n_r][n_c] = '1'
    new_new_swan_2 = copy.deepcopy(new_swan_2)
    while new_swan_2:
        if is_ans:
            break
        r, c = new_swan_2.pop()
        for g_r, g_c in go:
            n_r = r + g_r
            n_c = c + g_c
            if 0 <= n_r < R and 0 <= n_c < C:
                if lake[n_r][n_c] == '1':
                    is_ans = True
                    print(ans)
                    break
                if lake[n_r][n_c] == '.':
                    new_swan_2.append((n_r, n_c))
                    new_new_swan_2.append((n_r, n_c))
                    lake[n_r][n_c] = '2'     
    swan_n = copy.deepcopy(new_swan_n)
    swan_1 = copy.deepcopy(new_new_swan_1)
    swan_2 = copy.deepcopy(new_new_swan_2)