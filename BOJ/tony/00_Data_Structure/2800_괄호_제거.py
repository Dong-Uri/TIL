# 괄호쌍을 선택하는 모든 경우의 수를 만들어 내는 함수
def f(n, ghs):
    global allgh
    if n == gh_num:
        allgh += [ghs]
    else:
        f(n + 1, ghs)
        f(n+1, ghs + gh_set[n])

lst = list(input())
gh_set = []

# 괄호 쌍들의 집합
for idx, l in enumerate(lst):
    if l == '(':
        gh_set.append([idx])
    if l == ')':
        i = 1
        while True:
            if len(gh_set[-i]) == 1:
                gh_set[-i].append(idx)
                break
            i += 1

gh_num = len(gh_set)
allgh = [] # 모든 괄호쌍 경우의 수
f(0, [])
ans = []

# 모든 괄호쌍 경우의 수에 대해 괄호쌍들 제거
for i in range(1, len(allgh)):  # 빈 리스트인 0번 인덱스는 제외
    allgh[i].sort(reverse=True) # 내림차순 정렬
    n_lst = lst[:]              # 얕은 복사
    for j in allgh[i]:
        n_lst.pop(j)
    ans.append(''.join(n_lst))

# 나올수 있는 식들을 정렬후 중복을 제외하고 출력
ans.sort()
no_repeat = ''
for i in range(len(ans)):
    if no_repeat != ans[i]:
        print(ans[i])
        no_repeat = ans[i]