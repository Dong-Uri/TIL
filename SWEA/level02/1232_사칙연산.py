# 트리를 연산하는 함수
def calc(n):
    # 잎 노드에 저장된 값은 숫자형이므로 int로 출력
    if node[n].isnumeric():
        return int(node[n])
    # 그외 노드는 자식 노드에 대한 계산 값을 출력
    else:
        if node[n] == '+':
            return calc(ch1[n]) + calc(ch2[n])
        if node[n] == '-':
            return calc(ch1[n]) - calc(ch2[n])
        if node[n] == '*':
            return calc(ch1[n]) * calc(ch2[n])
        else:
            return calc(ch1[n]) / calc(ch2[n])

for t in range(1, 11):
    N = int(input())
    node = [0] * (N+1)
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    for _ in range(N):
        n = list(input().split())
        n[0] = int(n[0])
        node[n[0]] = n[1]
        # 연산자인 노드는 자식 노드값도 저장해 줌
        if not n[1].isnumeric():
            ch1[n[0]] = int(n[2])
            ch2[n[0]] = int(n[3])
    print(f'#{t} {int(calc(1))}')