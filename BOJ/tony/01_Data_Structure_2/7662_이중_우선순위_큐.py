import sys
import heapq
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    k = int(sys.stdin.readline().rstrip())
    minq = []
    maxq = []
    check = [0] * 1000000
    for i in range(k):
        calc, n = sys.stdin.readline().rstrip().split()
        n = int(n)
        if calc == 'I':
            heapq.heappush(minq, (n, i))
            heapq.heappush(maxq, (-n, i))
            check[i] = 1
        else:
            if n == 1:
                while maxq:
                    m, j = heapq.heappop(maxq)
                    if check[j]:
                        check[j] = 0
                        break
            else:
                while minq:
                    m, j = heapq.heappop(minq)
                    if check[j]:
                        check[j] = 0
                        break
    is_max = is_min = False
    while maxq:
        max_n, j = heapq.heappop(maxq)
        if check[j]:
            is_max = True
            check[j] = 0
            break
    while minq:
        min_n, j = heapq.heappop(minq)
        if check[j]:
            is_min = True
            check[j] = 0
            break
    if is_max and is_min:
        print(-max_n, min_n)
    elif is_max:
        print(-max_n, -max_n)
    else:
        print('EMPTY')