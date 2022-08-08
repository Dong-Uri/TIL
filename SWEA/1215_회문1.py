answer = []
for _ in range(10):
    palindrome_len = int(input())
    word_pan = []
    palindrome_num = 0 # 회문 개수
    for _ in range(8):
        word_line = input()
        word_pan.append(word_line)
        # 가로 회문 찾기 (글자판 만들면서 동시에 찾겠습니다.)
        for i in range(9-palindrome_len):
            check_word = '' # 회문인지 체크할 단어
            for j in range(palindrome_len):
                check_word += word_line[i+j]
            if check_word == check_word[::-1]: # 단어를 역순으로 해도 같은지 == 회문인지
                palindrome_num += 1
    # 세로 회문 찾기
    for k in range(8):
        for i in range(9-palindrome_len):
            check_word = '' # 회문인지 체크할 단어
            for j in range(palindrome_len):
                check_word += word_pan[i+j][k]
            if check_word == check_word[::-1]: # 단어를 역순으로 해도 같은지 == 회문인지
                palindrome_num += 1
    answer.append(palindrome_num)
for l in range(10):
    print(f'#{l+1} {answer[l]}')