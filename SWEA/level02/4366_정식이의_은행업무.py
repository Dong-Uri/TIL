T = int(input())
for t in range(1, T+1):
    wrong_num_2 = input()
    wrong_num_3 = input()
    
    # 틀린 이진수에 대한 십진수를 구함
    i = 0
    wrong_num_10 = 0
    for n in wrong_num_2[::-1]:
        wrong_num_10 += int(n) * (2 ** i)
        i += 1
    
    # 틀린 이진수에 대한 맞는 십진수 리스트를 만듦
    num_10s = []
    for i in range(len(wrong_num_2)):
        if wrong_num_2[- i - 1] == '1':
            num_10s.append(wrong_num_10 - 2 ** i)
        else:
            num_10s.append(wrong_num_10 + 2 ** i)
            
    # 십진수 후보중 삼진수와 한자리가 틀린 값을 찾음
    for num_10 in num_10s:
        ans = num_10
        wrong = 0
        num_3 = ''
        for wrong_n in wrong_num_3[::-1]:
            if wrong_n != str(num_10 % 3):
                wrong += 1
            num_3 += str(num_10 % 3)
            num_10 //= 3
        if wrong == 1:
            break
            
    print(f'#{t} {ans}')