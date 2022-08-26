# 패턴을 찍어내는 함수
def f(lst):
    ans = []
    for i in lst:
        ans += [i * 3]
    for i in lst:
        ans += [i + ' ' * len(lst[0]) + i]
    for i in lst:
        ans += [i * 3]
    return ans

N = int(input())
patt = ['*']

# N이 될때까지 f
while len(patt[0]) < N:
    patt = f(patt)
    
for i in patt:
    print(i)