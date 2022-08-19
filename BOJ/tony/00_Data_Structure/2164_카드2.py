N = int(input())
lst = [n+1 for n in range(N)]
while len(lst) > 1:
    if len(lst) % 2:
        lst = [lst[-1]] + lst[1::2]
    else:
        lst = lst[1::2]
print(lst[0])