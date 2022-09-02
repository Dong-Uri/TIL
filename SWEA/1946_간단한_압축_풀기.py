T = int(input())
Ns = []
zips = []
for t in range(1, T+1):
    N = int(input())
    zip = [[x for x in input().split()] for i in range(N)]

    # 일단 압축을 풀어줌
    unzip = ''
    for z in zip:
        unzip += z[0]*int(z[1])

    # 열줄씩 출력
    print(f'#{t}')
    for i in range(((len(unzip)-1)//10)+1):
        if i == len(unzip)//10:
            print(unzip[i*10:])
        else:
            print(unzip[i*10:(i+1)*10])