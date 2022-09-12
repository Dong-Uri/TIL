for _ in range(10):
    t = int(input())
    q = list(map(int, input().split()))
    key = 0
    while True:
        key += 1
        n = q.pop(0) - key

        # 0보다 작아지면 프로그램 종료
        if n <= 0:
            q.append(0)
            break
            
        # 일반적인 경우
        else:
            q.append(n)

        # 키가 5이면 0으로 재설정하여 새로운 사이클
        if key == 5:
            key = 0
            
    print(f'#{t}', *q)