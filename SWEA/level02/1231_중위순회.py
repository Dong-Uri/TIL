# 중위 순회하는 함수
def inorder(n):
    if 1 <= n <= N:
        inorder(child1[n])
        ans.append(alphabet[n])
        inorder(child2[n])

for t in range(1, 10):
    N = int(input())

    # 정점에 대한 정보 입력 및 정리
    alphabet = [''] * (N + 1)
    child1 = [0] * (N + 1)
    child2 = [0] * (N + 1)
    for _ in range(N):
        info = list(input().split())
        n = int(info[0])
        alphabet[n] = info[1]
        if len(info) >= 3:
            child1[n] = int(info[2])
        if len(info) >= 4:
            child2[n] = int(info[3])

    # 중위 순회하여 답 출력
    ans = []
    inorder(1)
    print(f'#{t}', ''.join(ans))