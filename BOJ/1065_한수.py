N = int(input())

# 99까지는 모두 한수
if N <= 99:
    print(N)
    
else:
    ans = 99
    for i in range(100, N+1):
        cha = (i % 10) - ((i // 10) % 10)           # 기준 차
        i //= 10
        while i // 10:
            if (i % 10) - ((i // 10) % 10) != cha:  # 차가 다르면 등차가 아님
                break
            i //= 10
        else:
            ans += 1                                # 차가 모두 같았으면 등차
    print(ans)