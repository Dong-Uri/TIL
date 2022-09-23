T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    Hs = list(map(int, input().split()))
    ans = 200000
    # 비트연산을 이용해 모든 경우의 수 풀이
    for i in range(1, 2 ** N):
        top = 0
        for j in range(N):
            if i & 1 << j:
                top += Hs[j]
            if top >= ans:  # 기존 답보다 큰 탑이라면 종료
                break
        if B <= top < ans:  # 기존 답보다 좋은 결과라면 저장
            ans = top
    print(f'#{t} {ans-B}')