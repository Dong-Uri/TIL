T = int(input())
for t in range(1, T+1):
    N = int(input())
    AB_list = [list(map(int, input().split())) for _ in range(N)]
    nosuns = [0] * 5000 # 몇개의 노선이 지나는지를 저장할 정류장들의 리스트
    for i in range(N):
        for n in range(AB_list[i][0] - 1, AB_list[i][1]):  # Ai-1 부터 Bi-1 까지
            nosuns[n] += 1 # i+1번째 노선이 지나는 정류장에 1을 더해줌
    P = int(input())
    ans_list = [0] * P
    for j in range(P):
        C = int(input())
        ans_list[j] = nosuns[C-1]
    print(f'#{t}', *ans_list)