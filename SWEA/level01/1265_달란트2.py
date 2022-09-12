T = int(input())
for t in range(1, T+1):
    N, P = map(int, input().split())
    
    # 균등하게 나눈 몫을 리스트로 만듦
    div = [N // P] * P
    
    # 나머지를 리스트 앞에서 부터1씩 더해줌
    for i in range(N % P):
        div[i] += 1
    
    # 리스트를 모두 곱함
    ans = 1
    for i in div:
        ans *= i
        
    print(f'#{t} {ans}')