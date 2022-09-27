import sys
import heapq
N = int(sys.stdin.readline().rstrip())
level = [[[], []] for _ in range(101)]
div = dict()
problem = [0] * 100001
for _ in range(N):
    P, L, G = map(int, sys.stdin.readline().rstrip().split())
    if G not in div.keys():
        div[G] = [[], []]
    heapq.heappush(div[G][0], (L, P))
    heapq.heappush(div[G][1], (-L, -P))
    heapq.heappush(level[L][0], P)
    heapq.heappush(level[L][1], -P)
    problem[P] = [L, G]
M = int(sys.stdin.readline().rstrip())
for i in range(M):
    command = list(sys.stdin.readline().rstrip().split())
    if command[0] == 'recommend':
        G = int(command[1])
        if command[2] == '1':
            while div[G][1]:
                L, P = heapq.heappop(div[G][1])
                L = -L
                P = -P
                if problem[P] == 0 or problem[P] != [L, G]:
                    continue
                print(P)
                heapq.heappush(div[G][1], (-L, -P))
                break
        else:
            while div[G][0]:
                L, P = heapq.heappop(div[G][0])
                if problem[P] == 0 or problem[P] != [L, G]:
                    continue
                print(P)
                heapq.heappush(div[G][0], (L, P))
                break
    elif command[0] == 'recommend2' or command[0] == 'recommend3':
        if command[0] == 'recommend2':
            if command[1] == '1':
                datum = 101
            else:
                datum = 1
        else:
            datum = int(command[2])
        out = False
        if (command[0] == 'recommend2' and command[1] == '1') or (command[0] == 'recommend3' and command[1] == '-1'):
            for i in range(datum - 1, 0, -1):
                while level[i][1]:
                    P = heapq.heappop(level[i][1])
                    P = -P
                    if problem[P] == 0 or problem[P][0] != i:
                        continue
                    print(P)
                    out = True
                    heapq.heappush(level[i][1], -P)
                    break
                if out:
                    break
            else:
                print(-1)
        else:
            for i in range(datum, 101):
                while level[i][0]:
                    P = heapq.heappop(level[i][0])
                    if problem[P] == 0 or problem[P][0] != i:
                        continue
                    print(P)
                    out = True
                    heapq.heappush(level[i][0], P)
                    break
                if out:
                    break
            else:
                print(-1)
    elif command[0] == 'add':
        P = int(command[1])
        L = int(command[2])
        G = int(command[3])
        if G not in div.keys():
            div[G] = [[], []]
        heapq.heappush(div[G][0], (L, P))
        heapq.heappush(div[G][1], (-L, -P))
        heapq.heappush(level[L][0], P)
        heapq.heappush(level[L][1], -P)
        problem[P] = [L, G]
    else:
        P = int(command[1])
        problem[P] = 0