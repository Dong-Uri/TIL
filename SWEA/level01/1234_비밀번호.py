for t in range(1, 11):
    _, strng = input().split()
    s = 0

    # 문자열 뒤에서 두번째 자리까지 연속 문자를 확인함
    while s < len(strng)-1:

        # 연속 문자 일때
        if strng[s] == strng[s+1]:
            strng = strng[:s] + strng[s+2:]

            # 찾은 연속 문자 이전부터 다시 찾기 진행
            if s != 0: # 시작부터 연속 문자면 그대로 시작부터 진행
                s -= 1

        # 연속 문자가 아니면 다음 자리 확인
        else:
            s += 1

    print(f'#{t} {strng}')