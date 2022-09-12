T = int(input())
for t in range(1, T+1):
    A, B = input().split()
    a = len(A)
    b = len(B)
    cnt = n = 0
    while n <= a-b:
        if A[n:n+b] == B:
            cnt += 1
            n += b
        else:
            n += 1
    print(f'#{t} {a-cnt*(b-1)}')