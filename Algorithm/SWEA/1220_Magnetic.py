answer = []
for _ in range(10):
    _ = input() # 100... 입력 왜받는데... 문제 번호로라도 해줘....
    test_case = []
    for _ in range(100):
        line = list(map(int, input().split()))
        test_case.append(line)
    gyochak_num = 0 # 제가 이런 한글리쉬 변수를 많이씁니다..
    for i in range(100):
        check_col = [] # N,S극이 위아래에 있어 열별로 체크합니다.
        for j in range(100):
            if test_case[j][i] in [1,2]: # 빈칸(0)이 아닌 1, 2라면
                check_col.append(test_case[j][i]) # 체크 열에 추가
        pre_jisungche = 0 # 확인할 지성체의 이전 지성체를 저장할 변수
        for jisungche in check_col:
            if pre_jisungche == 1 and jisungche == 2: # 지성체 1과 2가 배치되어 있는 경우 == 교착상태
                gyochak_num += 1
            pre_jisungche = jisungche # 지금 지성체를 이전 지성체에 저장
    answer.append(gyochak_num)
for l in range(10):
    print(f'#{l+1} {answer[l]}')