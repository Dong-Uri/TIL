from collections import deque

N, K = map(int, input().split())
subin = deque()
subin.append((N, 0))
young = []
young.append(K)
i = 0
y_list = [-1] * 500001
while K <= 500000:
    y_list[K] = i
    K += i + 1
    i += 1
ans = -1
visited_even = [False] * 500001
visited_odd = [False] * 500001
visited_even[N] = True
while subin:
    n, cnt = subin.popleft()
    if ans != -1 and cnt > ans:
        break
    if y_list[n] != -1 and y_list[n] >= cnt and (y_list[n] - cnt) % 2 == 0:
        if ans == -1 or y_list[n] < ans:
            ans = y_list[n]
    cnt += 1
    if cnt % 2:
        if n != 0 and not visited_odd[n-1]:
            subin.append((n - 1, cnt))
            visited_odd[n - 1] = True
        if n != 500000 and not visited_odd[n+1]:
            subin.append((n + 1, cnt))
            visited_odd[n + 1] = True
        if n*2 <= 500000 and not visited_odd[n*2]:
            subin.append((n * 2, cnt))
            visited_odd[n * 2] = True
    else:
        if n != 0 and not visited_even[n-1]:
            subin.append((n - 1, cnt))
            visited_even[n - 1] = True
        if n != 500000 and not visited_even[n+1]:
            subin.append((n + 1, cnt))
            visited_even[n + 1] = True
        if n*2 <= 500000 and not visited_even[n*2]:
            subin.append((n * 2, cnt))
            visited_even[n * 2] = True
print(ans)
