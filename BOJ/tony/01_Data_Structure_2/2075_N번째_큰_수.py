import sys
N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
i = [N - 1] * N
line = arr[-1]
cnt = 0
while True:
    cnt += 1
    if cnt == N:
        print(max(line))
        break
    max_j = line.index(max(line))
    i[max_j] -= 1
    line[max_j] = arr[i[max_j]][max_j]