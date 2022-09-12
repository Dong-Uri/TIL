T = int(input())
for t in range(1, T+1):
    max_len = 0
    word_list = []

    # 단어들을 입력받으며 가장 긴 문자열 길이를 찾음
    for _ in range(5):
        word = list(input())
        if len(word) > max_len:
            max_len = len(word)
        word_list += [word]

    # 단어들에 *을 넣어 가장 긴 문자열과 길이를 맞춤
    for i in range(5):
        word_list[i] += ['*'] * (max_len - len(word_list[i]))

    # *을 제외한 문자열들을 세로 순서로 모음
    ans = ''
    for i in range(max_len):
        for j in range(5):
            if word_list[j][i] != '*':
                ans += word_list[j][i]

    print(f'#{t} {ans}')