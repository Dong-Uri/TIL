N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))
origin_P = P
cnt = 0
while True:

    # 카드가 특정한 플레이어에게 보내지는 상태인지 확인
    for k in range(0, N, 3):
        if P[k] != 0 or P[k+1] != 1 or P[k+2] != 2:
            break
    else:
        ans = cnt
        break

    cnt += 1

    # 카드를 섞어 다시 P에 저장
    shuffle = [0] * N
    for i, j in enumerate(S):
        shuffle[j] = P[i]
    P = shuffle

    # 원래 P로 돌아왔다면 원하는데로 섞는 것이 불가능하므로 -1
    if P == origin_P:
        ans = -1
        break
        
print(ans)