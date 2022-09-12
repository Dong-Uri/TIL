V, E = map(int, input().split())
K = int(input().rstrip())
way = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    way[u].append([v, w-1])
ans = ['INF'] * V
visited = [0] * (V+1)
visited[K] = 1
q = [[K]]
t = -1
while q:
    t += 1
    go = q.pop(0)
    if not go:
        continue
    for i in go:
        ans[i-1] = t # 큐에서 나온 위치에 현재 시각 추가
        for j in way[i]:

            # 방문하지 않은 곳을 가중치 이후에 나오도록 큐에 저장
            if visited[j[0]] == 0:
                while j[1]+1 > len(q):
                    q.append([])
                q[j[1]].append(j[0])
                visited[j[0]] = 1

            # 방문한 곳이지만 더 빠르게 도착 할수 있어도 큐에 저장
            else:
                if j[1]+1 < len(q):
                    for k in range(j[1]+1, len(q)):
                        if j[0] in q[k]:
                            q[k].remove(j[0])
                            q[j[1]].append(j[0])

for i in range(V):
    print(ans[i])