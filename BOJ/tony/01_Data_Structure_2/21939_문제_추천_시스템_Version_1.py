import sys
import heapq
N = int(sys.stdin.readline().rstrip())
hard = []
easy = []
problem = [0] * 100001
for _ in range(N):
    P, L = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(easy, (L, P))
    heapq.heappush(hard, (-L, -P))
    problem[P] = L
M = int(sys.stdin.readline().rstrip())
for i in range(M):
    command = list(sys.stdin.readline().rstrip().split())
    if command[0] == 'recommend':
        if command[1] == '1':
            while hard:
                L, P = heapq.heappop(hard)
                L = -L
                P = -P
                if problem[P] == 0 or problem[P] != L:
                    continue
                print(P)
                heapq.heappush(hard, (-L, -P))
                break
        else:
            while easy:
                L, P = heapq.heappop(easy)
                if problem[P] == 0 or problem[P] != L:
                    continue
                print(P)
                heapq.heappush(easy, (L, P))
                break
    elif command[0] == 'add':
        P = int(command[1])
        L = int(command[2])
        heapq.heappush(easy, (L, P))
        heapq.heappush(hard, (-L, -P))
        problem[P] = L
    else:
        P = int(command[1])
        problem[P] = 0