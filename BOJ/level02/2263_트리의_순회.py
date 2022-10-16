import sys
n = int(sys.stdin.readline().rstrip())
inorder = list(map(int, sys.stdin.readline().rstrip().split()))
postorder = list(map(int, sys.stdin.readline().rstrip().split()))
ans = []
stk = [[0, n, 0, n]]
while stk:
    s_in, e_in, s_post, e_post= stk.pop()
    root = postorder[e_post-1]
    i = inorder[s_in:e_in].index(root)
    ans.append(root)
    if root != inorder[e_in-1]:
        stk.append([s_in + i + 1, e_in, s_post + i, e_post - 1])
    if root != inorder[s_in]:
        stk.append([s_in, s_in + i, s_post, s_post + i])
print(*ans)