for _ in range(10):
    t, N = map(int, input().split())
    arr = list(map(int, input().split()))

    # 가이드에 따른 데이터 저장
    way1 = [-1] * 100
    way2 = [-1] * 100
    for n in range(N):
        if way1[arr[2*n]] == -1:
            way1[arr[2*n]] = arr[2*n+1]
        else:
            way2[arr[2*n]] = arr[2*n+1]
    stk = []
    now = ans = 0
    while True:

        # 99에 도달시
        if now == 99:
            ans = 1
            break

        # 첫번째 데이터에 향할 정점이 있을때
        if way1[now] != -1:
            stk.append(now)
            now = way1[now]
            way1[stk[-1]] = -1

        # 두번째 데이터에 향할 정점이 있을때
        elif way2[now] != -1:
            stk.append(now)
            now = way2[now]
            way2[stk[-1]] = -1
            
        # 향할 정점이 없을때
        else:
            now = stk.pop()
        
        # 스택이 모두 소모되었을때
        if not stk:
            break
            
    print(f'#{t} {ans}')