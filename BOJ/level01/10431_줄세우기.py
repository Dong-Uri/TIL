P = int(input())
for _ in range(P):
    tall = list(map(int, input().split()))
    jul = []
    n = ans = 0
    for i in range(1, 21):
        
        # 줄 검사
        for j in range(n):
            if jul[j] > tall[i]:
                jul = jul[:j] + [tall[i]] + jul[j:]
                ans += n - j
                break
        else:
            jul += [tall[i]]
            
        n += 1
    print(tall[0], ans)