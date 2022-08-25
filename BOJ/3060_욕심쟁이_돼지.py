T = int(input())
for _ in range(T):
    N = int(input())
    eat = list(map(int, input().split()))

    # 첫날 식사의합
    hap = 0
    for i in eat:
        hap += i

    day = 0
    while True:
        day += 1
        if hap > N:
            break
        hap *= 4 # 먹는 총량은 4배가 됨
    print(day)