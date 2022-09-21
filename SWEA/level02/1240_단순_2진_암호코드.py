T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    for _ in range(N):
        line = input()
        # 정보(1)가 있는 줄을 코드로 저장
        if '1' in line:
            code = line
    # 맨뒤의 1에서부터 코드를 읽음
    back_code = code.rstrip('0')[::-1]
    i = 0
    back_num = []
    while i < len(back_code):
        if back_code[i] == '0': # 0인 경우는 코드가 끝난 경우
            break
        c = back_code[i:i+7]
        if c == '1011000':
            back_num.append(0)
        elif c == '1001100':
            back_num.append(1)
        elif c == '1100100':
            back_num.append(2)
        elif c == '1011110':
            back_num.append(3)
        elif c == '1100010':
            back_num.append(4)
        elif c == '1000110':
            back_num.append(5)
        elif c == '1111010':
            back_num.append(6)
        elif c == '1101110':
            back_num.append(7)
        elif c == '1110110':
            back_num.append(8)
        elif c == '1101000':
            back_num.append(9)
        i += 7
        
    # 코드의 합을 구하면서 올바른 암호인지 체크를함
    hap = 0
    chk = 0
    for i, n in enumerate(back_num):
        hap += n
        if i % 2:
            chk += 3 * n
        else:
            chk += n
            
    if chk % 10:
        print(f'#{t} 0')
    else:
        print(f'#{t} {hap}')