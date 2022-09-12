a, b = map(int, input().split())
if [a,b] in [[1,2],[2,3],[3,1]]:
    print('B')
if [a,b] in [[1,3],[2,1],[3,2]]:
    print('A')