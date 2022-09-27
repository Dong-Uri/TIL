# 모든 경우의 수들을 곱해주는 함수
def f(i, mul):
    global max_mul
    # 백트래킹(가지치기)
    if mul <= max_mul:
        return
    if i == N:
        max_mul = mul
        return
    for j in range(N):  # 정렬을 했기 때문에 큰 수부터 곱함
        if used[arr[i][j][1]] == 0:
            used[arr[i][j][1]] = 1
            f(i + 1, mul * arr[i][j][0] / 100)
            used[arr[i][j][1]] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    max_mul = 0

    # 값과 열번호를 저장한 후 내림차순 정렬
    arr = [[] for _ in range(N)]
    for i in range(N):
        line = list(map(int, input().split()))
        for j, n in enumerate(line):
            arr[i].append((n,j))
            arr[i].sort(reverse=True)
            
    used = [0] * N
    f(0, 1)
    print(f'#{t} {max_mul * 100:.6f}')