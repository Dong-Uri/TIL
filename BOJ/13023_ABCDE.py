# 다섯 친구의 케이스가 있는지 찾는 함수
def f():
    for i in range(N):
        stk = [i]
        for f1 in friend[i]:
                stk.append(f1)
                for f2 in friend[f1]:
                    if f2 != i:
                        stk.append(f2)
                        for f3 in friend[f2]:
                            if f3 != i and f3 != f1:
                                stk.append(f3)
                                for f4 in friend[f3]:
                                    if f4 != i and f4 != f1 and f4 != f2:
                                        return 1
    return 0

N, M = map(int, input().split())
friend = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)
print(f())