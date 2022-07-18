T = int(input())
Ns = []
zips = []
for _ in range(T):
    N = int(input())
    Ns.append(N)
    zip = [[x for x in input().split()] for i in range(N)]
    zips.append(zip)

for i in range(T):
    print('#%s'%(i+1))
    unzip = ''
    for z in zips[i]:
        unzip += z[0]*int(z[1])
    for i in range(((len(unzip)-1)//10)+1):
        if i == len(unzip)//10:
            print(unzip[i*10:])
        else:
            print(unzip[i*10:(i+1)*10])