T = int(input())
alien_num_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
answer = []
for _ in range(T):
    _ = input()
    testcase_line = input()
    testcase = list(testcase_line.split())
    num_list = []
    for alien_num in testcase:
        num_list.append(alien_num_list.index(alien_num))
        # alien_num_list에서 외계숫자와 인덱스가 일치하므로 인덱스를 num_list에 append함
    num_list.sort() # 정렬
    ans = []
    for num in num_list:
        ans.append(alien_num_list[num]) # 이번엔 인덱스에서 외계숫자로
    answer.append(' '.join(ans)) # ans는 출력조건의 문자열로 바꿔 저장해둠
for l in range(T):
    print(f'#{l+1} {answer[l]}')

# 테스트 하는데 뭔가 문제가 있다.
# Notion에 적어놓았음