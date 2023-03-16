import sys

N = int(sys.stdin.readline().rstrip())
connect = []
cross = [0] * N
for _ in range(N):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    connect.append([A, B])
connect.sort()
lst = []
dp = [0] * N
l = 0
for i in range(len(connect)):
    for j in range(len(lst)):
        if connect[i][1] < lst[j][1]:
            lst[j] = connect[i]
            dp[i] = j
            break
    else:
        lst.append(connect[i])
        dp[i] = l
        l += 1
print(N - l)
l -= 1
cut = []
for i in range(N-1, -1, -1):
    if dp[i] == l:
        l -= 1
    else:
        cut.append(connect[i][0])
for i in range(len(cut)-1, -1, -1):
    print(cut[i])