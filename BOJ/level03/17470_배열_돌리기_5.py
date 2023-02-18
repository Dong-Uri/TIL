import sys

def swap(x, y):
    global stat
    temp = stat[x]
    stat[x] = stat[y]
    stat[y] = temp

def rot(arr, turn, flip):
    if flip:
        for i in range(len(arr)):
            arr[i] = arr[i][::-1]
    for _ in range(turn):
        arr = list(map(list, zip(*arr[::-1])))
    return arr

N, M, R = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
stat = [0, 1, 2, 3, 4, 0]
Rs = list(map(int, sys.stdin.readline().rstrip().split()))
for work in Rs:
    if work == 1:
        swap(1, 4)
        swap(2, 3)
        if stat[0] == 0:
            stat[0] = 2
        elif stat[0] == 2:
            stat[0] = 0
        stat[5] = 1 - stat[5]
    elif work == 2:
        swap(1, 2)
        swap(3, 4)
        if stat[0] == 1:
            stat[0] = 3
        elif stat[0] == 3:
            stat[0] = 1
        stat[5] = 1 - stat[5]
    elif work == 3 or work == 5:
        temp = stat[4]
        stat[4] = stat[3]
        stat[3] = stat[2]
        stat[2] = stat[1]
        stat[1] = temp
        if work == 3:
            stat[0] += 1
            if stat[0] == 4:
                stat[0] = 0
    elif work == 4 or work == 6:
        temp = stat[1]
        stat[1] = stat[2]
        stat[2] = stat[3]
        stat[3] = stat[4]
        stat[4] = temp
        if work == 4:
            stat[0] -= 1
            if stat[0] == -1:
                stat[0] = 3
arrs = [[],[],[],[]]
for i in range(N//2):
    arrs[0].append(arr[i][:M//2])
    arrs[1].append(arr[i][M//2:])
for i in range(N//2, N):
    arrs[3].append(arr[i][:M//2])
    arrs[2].append(arr[i][M//2:])
new_arrs = [[],[],[],[]]
for i in range(4):
    new_arrs[i] = rot(arrs[stat[i+1]-1], stat[0], stat[5])
if stat[0] % 2:
    x = M // 2
else:
    x = N // 2
for i in range(x):
    print(*(new_arrs[0][i] + new_arrs[1][i]))
for i in range(x):
    print(*(new_arrs[3][i] + new_arrs[2][i]))