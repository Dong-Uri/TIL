import sys
n = int(sys.stdin.readline().rstrip())
connect = [[] for _ in range(n+1)]
for _ in range(n):
    lst = list(map(int, sys.stdin.readline().rstrip().split()))
    m = lst[0]
    i = 1
    while lst[i] != -1:
        connect[m].append([lst[i], lst[i+1]])
        i += 2
visited = [0] * (n+1)
stk = [1]
visited[1] = 1
parent = [[i, 0, 0, 0] for i in range(n+1)]
while stk:
    now = stk.pop()
    for c in connect[now]:
        if visited[c[0]] == 0:
            parent[c[0]] = [c[0], now, c[1], parent[now][3] + 1]
            stk.append(c[0])
            visited[c[0]] = 1
parent.sort(key=lambda x: x[3], reverse=True)
length = [[0, 0] for _ in range(n+1)]
for ch, pr, l, _ in parent:
    ls = l + max(length[ch])
    if length[pr][0] <= length[pr][1] and ls > length[pr][0]:
        length[pr][0] = ls
    elif length[pr][0] >= length[pr][1] and ls > length[pr][1]:
        length[pr][1] = ls
ans = 0
for a, b in length[1:]:
    if a + b > ans:
        ans = a + b
print(ans)