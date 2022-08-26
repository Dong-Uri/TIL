import sys
N = int(sys.stdin.readline().rstrip())
lst = [0] * 2020001 # x축의 -1010000부터 1010000까지

# x축에 양쪽 지름에 대한 정보를 추가
ans = 'YES'
for i in range(N):
    x, r = map(int, sys.stdin.readline().rstrip().split())

    # 지름이 만나는 경우 교점이 있는 것이므로 NO
    if lst[x - r + 1010000] != 0 or lst[x + r + 1010000] != 0:
        ans = 'NO'
        break

    lst[x - r + 1010000] = [i, 'in']
    lst[x + r + 1010000] = [i, 'out']

# 원의 시작과 끝의 포함관계 조사 (괄호문제 참고)
if ans == 'YES':
    stk = []
    for i in lst:
        if i != 0:
            if i[1] == 'in':
                stk.append(i[0])
            else:
                if i[0] == stk[-1]:
                    stk.pop()
                else:
                    ans = 'NO'
                    break
                    
print(ans)