N, K = map(int, input().split())
note = [list(input().split()) for _ in range(K)]
wheel = ['?'] * N
alp_list = []
i = 0
for K, alp in note[::-1]: # 뒤에서부터 바퀴에 알파벳을 넣음

    # 아직 모르는 위치일때
    if wheel[i] == '?':
        wheel[i] = alp

        # 하지만 알파벳이 이미 나온 알파벳 일때
        if alp in alp_list:
            ans = '!'
            break

        alp_list.append(alp)

    # 이미 알던 위치일때
    elif wheel[i] == alp:
        pass

    # 알고있던 알파벳과 다를때
    else:
        ans = '!'
        break

    # 다음 바퀴칸 계산
    i = (i + int(K)) % N

else:
    ans = ''.join(wheel)
print(ans)