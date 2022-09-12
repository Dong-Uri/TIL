N = int(input())
lst = [x for x in range(1,N+1)]
cnt = 0
fibo = [1, 1] # 피보나치 수열 사용
while lst: # 양수인 값이 없어서 빈리스트가 될때까지 반복
    cnt += 1
    last_lst = lst
    lst = []
    
    # 홀수번째 계산식
    if cnt%2:
        for i in last_lst:
            if fibo[-2] * N - fibo[-1] * i >= 0:
                lst.append(i)
                
    # 짝수번째 계산식
    else:
        for i in last_lst:
            if fibo[-1] * i - fibo[-2] * N >= 0:
                lst.append(i)
    fibo.append(fibo[-1] + fibo[-2])
    
print(cnt+1)
ans = [N, last_lst[0]]
for _ in range(cnt-1):
    ans.append(ans[-2]-ans[-1])
print(*ans)