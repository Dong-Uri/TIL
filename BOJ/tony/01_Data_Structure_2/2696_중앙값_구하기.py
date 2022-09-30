import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    M = int(sys.stdin.readline().rstrip())
    lst = []
    for _ in range(M//10+1):
        lst += list(map(int, sys.stdin.readline().rstrip().split()))
    sort_lst = []
    print_lst = []
    i = 0
    while i < M:
        sort_lst.append(lst[i])
        sort_lst.sort()
        if i % 2 == 0:
            print_lst.append(sort_lst[len(sort_lst)//2])
        i += 1
    l = len(print_lst)
    print(l)
    for i in range((l-1)//10+1):
        print(*print_lst[i*10:i*10+10])