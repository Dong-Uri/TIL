for _ in range(int(input())):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    page_num = [n for n in range(N)]
    cnt = 0
    while queue:
        now = queue.pop(0)
        page_now = page_num.pop(0)

        # 중요도 검사
        for q in queue:

            # 더 중요한 페이지가 있다면 다시 삽입
            if q >now:
               queue.append(now)
               page_num.append(page_now)
               break
        
        # 더 중요한 페이지가 없다면 인쇄
        else:
            cnt += 1
            
            # 인쇄 순서를 알고 싶은 페이지에 도달
            if page_now == M:
                print(cnt)
                break