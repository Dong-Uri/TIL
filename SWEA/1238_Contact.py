answer = []
for _ in range(10):
    long, start = map(int, input().split())
    fromto = [int(x) for x in input().split()]
    queue = [start]
    visited = [0 for i in range(100)]
    visited[start-1] = 1
    far = 2
    while len(queue) > 0:
        count = len(queue)
        for _ in range(count):
            now = queue.pop(0)
            for i in range(int(long/2)):
                if fromto[i*2] == now and visited[fromto[i*2+1]-1] == 0:
                    queue.append(fromto[i*2+1])
                    visited[fromto[i*2+1]-1] = far
        far += 1
    answer.append(100-visited[::-1].index(max(visited)))
for t in range(10):
    print('#%d %d'%((t+1), answer[t]))         