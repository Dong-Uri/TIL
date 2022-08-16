T = int(input())
for t in range(1, T+1):
    gualho = input()
    makde = 0
    ans = 0
    for i in range(len(gualho)-1):

        # ()가 아닌 (가 있는 경우는 막대의 시작 부분
        if gualho[i] == '(' and gualho[i+1] != ')':
            ans += 1 # 기본 막대 개수가 추가됨
            makde += 1 # 막대가 하나 쌓임

        # ()가 아닌 )가 있는 경우는 막대의 끝 부분
        elif gualho[i] == ')' and gualho[i-1] != '(':
            makde -= 1 # 막대가 하나 빠짐

        # ()인 경우는 레이저
        elif gualho[i] == '(' and gualho[i+1] == ')':
            ans += makde # 쌓여있는 막대들을 잘라 막대 개수가 추가됨

    print(f'#{t} {ans}')