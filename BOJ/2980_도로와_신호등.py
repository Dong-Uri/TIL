N, L = map(int, input().split())
wait = 0
for _ in range(N):
    D, R, G = map(int, input().split())
    t = (D + wait) % (R + G)    # 가는 시간 + 그동안 기다린 시간 == 신호등에 도달한 시간
    if t < R:                   # 도착한 시간이 사이클 내에서 빨간불일때
        wait += R - t           # 기다리는 시간 추가
print(L + wait)