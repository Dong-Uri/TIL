for t in range(1, 11):
    V, E = map(int, input().split())
    gansun = list(map(int, input().split()))
    ans = []
    while len(ans) < V:
        for i in range(1, V+1):
            possible = True
            for j in range(E):
                if gansun[2*j+1] == i:
                    possible = False
                    break
            for j in ans:
                if i == j:
                    possible = False
                    break
            if possible:
                ans += [i]
                for j in range(E):
                    if gansun[2*j] == i:
                        gansun[2 * j + 1] = 0
    print(f'#{t}', *ans)