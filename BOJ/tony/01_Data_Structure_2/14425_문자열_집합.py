import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
N_set = set(sys.stdin.readline().rstrip() for _ in range(N))
M_set = set()
M_dict = {}
for _ in range(M):
    m = sys.stdin.readline().rstrip()
    M_set = M_set | {m,}
    if m in M_dict.keys():
        M_dict[m] += 1
    else:
        M_dict[m] = 1
ans = 0
for i in N_set & M_set:
    ans += M_dict[i]
print(ans)