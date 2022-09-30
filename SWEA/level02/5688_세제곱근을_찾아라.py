T = int(input())
for t in range(1, T+1):
    N = int(input())
    n = int(N ** (1/3))         # 세제곱근의 정수형 (버림)
    if N == n ** 3:             # N의 세제곱근이 맞는 경우
        print(f'#{t} {n}')
    elif N == (n+1) **3:        # 계산 오차로 인해 1차이가 생길 수 있음
        print(f'#{t} {n+1}')
    else:                       # 세제곱근인 정수가 없는 경우
        print(f'#{t} -1')