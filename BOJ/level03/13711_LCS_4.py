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
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
lst_dict = dict()
for i in range(N):
    lst_dict[lst1[i]] = i
A = []
for a in lst2:
    A.append(lst_dict[a])
lst = [A[0]]
for i in range(1, N):
    last = lst[-1]
    if A[i] > last:
        lst.append(A[i])
        last = A[i]
        continue
    bs(0, len(lst), A[i])
print(len(lst))