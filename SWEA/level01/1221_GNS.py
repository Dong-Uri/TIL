T = int(input())
num_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
for t in range(1, T+1):
    _, N = input().split()
    N = int(N)
    testcase = list(input().split())
    cnt_list = [0] * 10
    for i in range(N):
        if testcase[i] == 'ZRO':
            cnt_list[0] += 1
        elif testcase[i] == 'ONE':
            cnt_list[1] += 1
        elif testcase[i] == 'TWO':
            cnt_list[2] += 1
        elif testcase[i] == 'THR':
            cnt_list[3] += 1
        elif testcase[i] == 'FOR':
            cnt_list[4] += 1
        elif testcase[i] == 'FIV':
            cnt_list[5] += 1
        elif testcase[i] == 'SIX':
            cnt_list[6] += 1
        elif testcase[i] == 'SVN':
            cnt_list[7] += 1
        elif testcase[i] == 'EGT':
            cnt_list[8] += 1
        elif testcase[i] == 'NIN':
            cnt_list[9] += 1
    ans = []
    idx = 0
    for i in cnt_list:
        for j in range(i):
            ans += [num_list[idx]]
        idx += 1
    print(f'#{t}')
    print(*ans)