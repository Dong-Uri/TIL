N = int(input())
tops = list(map(int, input().split()))
ans = [0] * N
stk = []

# 맨 오른쪽 탑부터 검사
for n in range(N):
    
    # 스택을 꺼내서 현재 탑보다 낮은 탑들에 표시
    while stk and tops[N - n - 1] > stk[-1][1]:
        ans[stk[-1][0]] = N - n
        stk.pop()

    # 탑의 인덱스와 높이를 스택에 넣음
    stk.append([N - n - 1, tops[N - n - 1]])
    
print(*ans)