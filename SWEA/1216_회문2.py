for _ in range(10):
    t = input()
    palindrome_len = 1 # 찾을 회문 길이
    word_pan = [input() for _ in range(100)]
    double_check = True
    breakout = False
    while True:
        palindrome_len += 1 # 1짜리 회문은 당연하므로 스킵
        for k in range(100):
            for i in range(101-palindrome_len):

                # 가로로된 단어가 회문인지
                check_word = ''
                for j in range(palindrome_len):
                    check_word += word_pan[k][i+j]
                if check_word == check_word[::-1]:
                    breakout = True 
                    break
                    
                # 세로로된 단어가 회문인지
                check_word = ''
                for j in range(palindrome_len):
                    check_word += word_pan[i+j][k]
                if check_word == check_word[::-1]:
                    breakout = True
                    break
                    
            if breakout: # break로 나왔다었다면
                double_check = True # 회문을 찾았다는 표시
                breakout = False # breakout은 초기화
                break # for문이 이중이라 한번더 break
                
        else: # 회문을 찾지 못해 break되지 않았을때
            if double_check: # 이전에는 회문을 찾았었다면
                double_check = False # 이번에는 못찾았음
            else: # 이전에도 회문을 못찾았다면
                break # 회문을 두번 연속 못찾으면 짝수, 홀수 회문이 더이상 없다는 의미
    
    print(f'#{t} {palindrome_len-2}') # 두번 못찾기 전의 회문이 최대 길이

# 시간초과
# for _ in range(10):
#     t = input()
#     palindrome_len = 101 # 처음 길이는 100이지만 시작할때 1을 빼고 시작하므로..
#     word_pan = []
#     for _ in range(100):
#         word_line = input()
#         word_pan.append(word_line)
#     palindrome_check = True
#     while palindrome_check: # 회문을 찾으면 False가 되어 끝낼 예정
#         palindrome_len -= 1 # 반복 시작시 길이가 하나 적은 회문을 찾음
#         # 가로 회문 찾기
#         for k in range(100):
#             for i in range(101-palindrome_len):
#                 check_word = '' # 회문인지 체크할 단어
#                 for j in range(palindrome_len):
#                     check_word += word_pan[k][i+j]
#                 if check_word == check_word[::-1]: # 단어를 역순으로 해도 같은지 == 회문인지
#                     palindrome_check = False
#                     break
#             if not palindrome_check :
#                 break # for문이 이중이라 한번더 break 해줍니다.
#         if palindrome_check : # 가로 회문을 못찾았을때만 돌립니다.
#             # 세로 회문 찾기
#             for k in range(100):
#                 for i in range(101-palindrome_len):
#                     check_word = '' # 회문인지 체크할 단어
#                     for j in range(palindrome_len):
#                         check_word += word_pan[i+j][k]
#                     if check_word == check_word[::-1]: # 단어를 역순으로 해도 같은지 == 회문인지
#                         palindrome_check = False
#                         break
#                 if not palindrome_check :
#                     break # for문이 이중이라 한번더 break 해줍니다.
#     print(f'#{t} {palindrome_len}')