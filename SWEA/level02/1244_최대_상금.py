T = int(input())
for C in range(1, T+1):
    num, chg = input().split()
    num_lst = []
    for n in num:
        num_lst.append(int(n))
    x = 0                   # 자리 변경 횟수
    while True:
        if x == int(chg):   # 자리 변경 횟수가 변경 가능 횟수에 도달하면 종료
            break
        i = 0               # 자리 변경 인덱스
        while True:

            # 자리 변경 인덱스가 끝까지 도달하였을때 (이미 값이 최대라는 의미)
            if i == len(num_lst):
                x += 1  # 일단 변경 횟수 추가
                # 중복되는 숫자가 있다면 그 둘을 바꿔 최대를 유지
                for j in range(i - 1):
                    if num_lst[j] == num_lst[j+1]:
                        break
                # 중복되는 숫자가 없다면 자리수가 가장 작은 마지막 두 수의 위치를 바꿈
                else:
                    num_lst[-1], num_lst[-2] = num_lst[-2], num_lst[-1]
                break

            max_num = max(num_lst[i:])
            if num_lst[i] == max_num:
                i += 1      # 자리 변경 인덱스가 수들 중 최대값이라면 자리를 바꾸지 않고 다음 인덱스의 자리를 바꿈
                continue

            # 최대값들의 개수 계산
            cnt = 0
            for n in num_lst[i+1:]:
                if max_num == n:
                    cnt += 1
            c = min(len(num_lst) - i - cnt, cnt, int(chg) - x)  # 최대값이 아닌 수의 개수, 최대값의 개수, 남은 자리 변경 횟수중 최소값
            x += c                                              # 그 수만큼 변경할 예정

            # c의 개수만큼 최대값이 아닌 수들을 최대값으로 바꿔주고 그 수는 리스트로 저장 후 정렬
            c_lst = []
            for _ in range(c):
                for k in range(i, len(num_lst)):
                    if num_lst[k] != max_num:
                        c_lst.append(num_lst[k])
                        num_lst[k] = max_num
                        break
            c_lst.sort()

            # 뒤에서 부터 최대값인 수들을 저장해 둔 최대값이 아닌 수들로 넣어줌
            for j in range(len(num_lst) - 1, i, -1):
                if num_lst[j] == max_num:
                    num_lst[j] = c_lst.pop(0)
                    c -= 1
                if c == 0:
                    break
                
            break
    ans = 0
    for i, n in enumerate(num_lst[::-1]):
        ans += n * (10 ** i)
    print(f'#{C} {ans}')