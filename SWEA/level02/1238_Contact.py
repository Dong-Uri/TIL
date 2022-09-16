for t in range(1,11):
    len, start = map(int, input().split())
    lst = list(map(int, input().split()))

    # 각각 인덱스에서 연락 할 수 있는 번호의 리스트를 작성
    from_to = [[] for _ in range(101)]
    for i in range(len//2):
        from_to[lst[i * 2]].append(lst[i * 2 + 1])

    # 큐를 통해 연락 순회
    called = [0] * 101
    called[start] = 1
    que = [start]
    while True:
        now = que.pop(0)
        for i in from_to[now]:
            if called[i] == 0:
                called[i] = called[now] + 1
                que.append(i)
        if not que:
            last = called[now]  # 마지막 전화가 몇번째인지 저장
            break

    # 마지막 전화를 받은 사람을 저장
    for i, x in enumerate(called):
        if x == last:
            ans = i # 최후에는 가장 큰 번호로 저장됨

    print(f'#{t} {ans}')