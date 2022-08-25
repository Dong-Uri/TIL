T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    print(f'#{t}')
    for i in range(N):
        arr90 = ''  # 90도 회전시 나올 배열의 한줄 문자열
        arr180 = '' # 180도 회전시 나올 배열의 한줄 문자열
        arr270 = '' # 270도 회전시 나올 배열의 한줄 문자열
        for j in range(N):
            arr90 += arr[N-j-1][i]
            arr180 += arr[N-i-1][N-j-1]
            arr270 += arr[j][N-i-1]
        print(arr90, arr180, arr270)