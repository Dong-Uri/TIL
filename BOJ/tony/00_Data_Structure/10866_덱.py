import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
dq = deque()
for _ in range(N):
    order = sys.stdin.readline().rstrip()
    if order[:10] == 'push_front':
        dq.appendleft(int(order[11:]))
    elif order[:9] == 'push_back':
        dq.append(int(order[10:]))
    elif order == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif order == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif order == 'size':
        print(len(dq))
    elif order == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif order == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)
    else:
        pass