T = int(input())
words = [input() for _ in range(T)]
for idx, word in enumerate(words):
    if word == word[::-1]:
        print('#%d 1'%(idx+1))
    else:
        print('#%d 0'%(idx+1))