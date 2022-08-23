import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
q = deque()
for _ in range(N):
    order = sys.stdin.readline().rstrip()
    if order[:4] == 'push':
        q.append(int(order[5:]))
    elif order == 'pop':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif order == 'size':
        print(len(q))
    elif order == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif order == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    else:
        pass

# 하위 문제
# 10845_큐