# 문제 오류로 input()에 모두 strip()을 붙여주었음

T = int(input().strip())
for t in range(1, T+1):
    N, M = map(int, input().strip().split())
    pw_16 = []
    for _ in range(N):
        line = input().strip().strip('0')

        # 0을 제거한 라인들을 중복 제거하여 저장
        if line and line not in pw_16:
            pw_16.append(line.strip('0'))

    dict_16to2 = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    cnt_01s = []
    ans = 0
    for pw in pw_16:

        # 16진수를 거꾸로된 2진수로
        pw_2 = ''
        for w in pw:
            pw_2 += dict_16to2[w]
        pw_2 = pw_2.strip('0')[::-1] + '00'

        # 0과 1의 개수를 배열로 저장
        cnt_01 = [0]
        now = '1'
        while pw_2:

            # 배열이 32개가 되는 경우
            if len(cnt_01) == 32:
                if cnt_01 not in cnt_01s:
                    cnt_01s.append(cnt_01)
                
                # 라인 내에 코드가 둘 이상 있는 경우를 위해 계속 진행함
                pw_2 = pw_2.lstrip('0')
                cnt_01 = [0]
                now = '1'
                continue

            elif pw_2[0] == now:
                cnt_01[-1] += 1
            else:
                now = pw_2[0]
                cnt_01.append(1)
            pw_2 = pw_2[1:]

    # 배열의 암호를 풀어줌
    for cnt in cnt_01s:
        x = min(cnt[0], cnt[2], cnt[3]) # 암호의 선이 x배로 굵어진 상태
        dict_code = {'112': '0', '122': '1', '221': '2', '114': '3', '231': '4', '132': '5', '411': '6', '213': '7', '312': '8', '211': '9'}
        amho = ''

        # 세 값의 비율로 암호값을 찾아냄
        for i in range(0, 32, 4):
            biyul = str(cnt[i] // x) + str(cnt[i+1] // x) + str(cnt[i+2] // x)
            amho += dict_code[biyul]

        # 만들어진 암호가 정상암호인지 확인 후 정답에 더함
        hap = 0
        chk = 0
        for i, n in enumerate(amho):
            if i % 2:
                hap += int(n)
                chk += 3 * int(n)
            else:
                hap += int(n)
                chk += int(n)
        if chk % 10 == 0:
            ans += hap
            
    print(f'#{t} {ans}')