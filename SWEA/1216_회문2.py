answer = []
for _ in range(10):
    _ = input()
    palindrome_len = 101 # 처음 길이는 100이지만 시작할때 1을 빼고 시작하므로..
    word_pan = []
    for _ in range(100):
        word_line = input()
        word_pan.append(word_line)
    palindrome_check = True
    while palindrome_check: # 회문을 찾으면 False가 되어 끝낼 예정
        palindrome_len -= 1 # 반복 시작시 길이가 하나 적은 회문을 찾음
        # 가로 회문 찾기
        for k in range(100):
            for i in range(101-palindrome_len):
                check_word = '' # 회문인지 체크할 단어
                for j in range(palindrome_len):
                    check_word += word_pan[k][i+j]
                if check_word == check_word[::-1]: # 단어를 역순으로 해도 같은지 == 회문인지
                    palindrome_check = False
                    break
            if not palindrome_check :
                break # for문이 이중이라 한번더 break 해줍니다.
        if palindrome_check : # 가로 회문을 못찾았을때만 돌립니다.
            # 세로 회문 찾기
            for k in range(100):
                for i in range(101-palindrome_len):
                    check_word = '' # 회문인지 체크할 단어
                    for j in range(palindrome_len):
                        check_word += word_pan[i+j][k]
                    if check_word == check_word[::-1]: # 단어를 역순으로 해도 같은지 == 회문인지
                        palindrome_check = False
                        break
                if not palindrome_check :
                    break # for문이 이중이라 한번더 break 해줍니다.
    answer.append(palindrome_len)
for l in range(10):
    print(f'#{l+1} {answer[l]}')