# 숫자 만드는 함수
def calc(num, pl, mi, mu, di, result, i):
    global max_result
    global min_result
    if i == N:
        print(result)
        if result > max_result:
            max_result = result
        if result < min_result:
            min_result = result
    # 각 연산자 카드가 있다면 사용
    if pl:
        calc(num, pl - 1, mi, mu, di, result + num[i], i + 1)
    if mi:
        calc(num, pl, mi - 1, mu, di, result - num[i], i + 1)
    if mu:
        calc(num, pl, mi, mu - 1, di, result * num[i], i + 1)
    if di:
        # 음수를 나눌때는 양수로 만들어 준 후에 진행
        if result < 0:
            calc(num, pl, mi, mu, di - 1, -((-result) // num[i]), i + 1)
        else:
            calc(num, pl, mi, mu, di - 1, result // num[i], i + 1)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    pl, mi, mu, di = map(int, input().split())
    num = list(map(int, input().split()))
    max_result = - 100000000
    min_result = 100000000
    calc(num, pl, mi, mu, di, num[0], 1)
    print(f'#{t} {max_result - min_result}')