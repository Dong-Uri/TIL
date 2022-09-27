tree_dict = {}
cnt = 0
while True:
    try:
        tree = input()
        cnt += 1
        if tree in tree_dict.keys():
            tree_dict[tree] += 1
        else:
            tree_dict[tree] = 1
    except:
        break
trees = sorted(tree_dict.items())
for t, n in trees:
    print(f'{t}{100 * n / cnt : .4f}')