T = int(input())
for t in range(1, T+1):
    N = int(input())
    abcde = [0] * 5 # a, b, c, d, e의 리스트
    yaksu = [2, 3, 5, 7, 11] # 약수의 리스트
    while N != 1:
        for i in range(5):
            while N % yaksu[i] == 0: # N이 약수로 나누어지는 동안
                N //= yaksu[i]
                abcde[i] += 1
    print(f'#{t}', *abcde)