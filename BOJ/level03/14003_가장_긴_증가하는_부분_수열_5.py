def bs(s, e, n):
    global lst
    global order
    if s == e:
        lst[s] = n
        order[i] = s + 1
        return
    m = (s + e) // 2
    if lst[m] == n:
        order[i] = m + 1
        return
    if lst[m] < n:
        bs(m + 1, e, n)
    if lst[m] > n:
        bs(s, m, n)

N = int(input())
A = list(map(int, input().split()))
lst = [A[0]]
order = [0] * N
order[0] = 1
l = 1
last = A[0]
for i in range(1, N):
    last = lst[-1]
    if A[i] > last:
        lst.append(A[i])
        last = A[i]
        l += 1
        order[i] = l 
        continue
    bs(0, len(lst), A[i])
ans = len(lst)
print(ans)
answer = []
N -= 1
while ans >= 1:
    if order[N] == ans:
        answer.append(A[N])
        ans -= 1
    N -= 1
print(*answer[::-1])