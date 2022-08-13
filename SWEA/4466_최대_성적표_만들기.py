T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    for i in range(K):
        max_score = scores[i]
        max_idx = i
        for j in range(i+1, N):
            if scores[j] > max_score:
                max_score = scores[j]
                max_idx = j
        scores[i], scores[max_idx] = scores[max_idx], scores[i]
    ans = 0
    for i in range(K):
        ans += scores[i]
    print(f'#{t} {ans}')