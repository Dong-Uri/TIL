def d(n):
    ans = n
    while n:
        ans += n % 10
        n //= 10
    return ans

lst = [n for n in range(1, 10001)]

# 셀프 넘버가 아닌 수 제거
for i in range(10000):
    if d(i) in lst:
        lst.remove(d(i))
        
for i in lst:
    print(i)