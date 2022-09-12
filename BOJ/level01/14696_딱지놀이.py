N = int(input())
for _ in range(N):
    A = [0] * 5
    B = [0] * 5
    a_arr = list(map(int, input().split()))
    b_arr = list(map(int, input().split()))
    
    # A, B에 카드를 index별로 정리
    for a in range(1, a_arr[0] + 1):
        A[a_arr[a]] += 1
    for b in range(1, b_arr[0] + 1):
        B[b_arr[b]] += 1
        
    # 4부터 1까지 카드의 세기 비교
    for i in range(4, 0, -1):
        if A[i] > B[i]:
            print('A')
            break
        elif B[i] > A[i]:
            print('B')
            break
    
    # for문이 모두 돌았다는건 비겼다는 의미
    else:
        print('D')