def bs(s, e, n):
    global lst
    if s == e:
        lst[s] = n
    m = (s + e) // 2
    if lst[m] == n:
        return
    if lst[m] < n:
        bs(m + 1, e, n)
    if lst[m] > n:
        bs(s, m, n)

N = int(input())
A = list(map(int, input().split()))
lst = [A[0]]
for i in range(1, N):
    last = lst[-1]
    if A[i] > last:
        lst.append(A[i])
        last = A[i]
        continue
    bs(0, len(lst), A[i])
print(len(lst))

# 하위 문제
# 12015_가장_긴_증가하는_부분_수열_2