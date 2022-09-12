# 파스칼의 다음 줄을 계산하는 함수
def pascal(arr):
    arr_n = [1] * (len(arr)+1)
    for i in range(1, len(arr)):
        arr_n[i] = arr[i-1] + arr[i]
    return arr_n

T = int(input())
for t in range(1, T+1):
    N = int(input())
    print(f'#{t}')
    ans = [1] # 파스칼 첫 줄
    print(*ans)
    for i in range(1, N):
        print(*pascal(ans))
        ans = pascal(ans)