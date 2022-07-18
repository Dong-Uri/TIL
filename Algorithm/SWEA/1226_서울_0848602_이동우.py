answer = []
for _ in range(10):
    n = input()
    maze = []
    for x in range(16):
        line = list(input())
        if '2' in line:
            startx = x
            starty = line.index('2')
        maze.append(line)
    stack = [[startx, starty]]
    ans = 0
    while len(stack) > 0 :
        now = stack.pop()
        x = now[0]
        y = now[1]
        if maze[x][y-1] == '3' or maze[x][y+1] == '3' or maze[x+1][y] == '3' or maze[x-1][y] == '3':
            ans = 1
            break
        if maze[x][y-1] == '0':
            stack.append([x,y-1])
            maze[x][y-1] = '2'
        if maze[x][y+1] == '0':
            stack.append([x,y+1])
            maze[x][y+1] = '2'
        if maze[x+1][y] == '0':
            stack.append([x+1,y])
            maze[x+1][y] = '2'
        if maze[x-1][y] == '0':
            stack.append([x-1,y])
            maze[x-1][y] = '2'
    answer.append(ans)
for t in range(10):
    print('#%d %s'%((t+1), answer[t]))