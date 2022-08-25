N = int(input())
hubo = [int(input()) for _ in range(N)]
ans = 0
while True:
    winner = 0
    win_vote = hubo[0]
    
    # 현재 투표 우승자
    for i in range(1, N):
        if hubo[i] >= win_vote:
            winner = i
            win_vote = hubo[i]
            
    # 승리하면 종료
    if winner == 0:
        break
        
    # 투표 조작
    hubo[0] += 1
    hubo[winner] -= 1
    ans += 1
    
print(ans)