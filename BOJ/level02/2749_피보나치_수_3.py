n = int(input())
n %= 1500000
fibo = [0] * (n+1)
if n == 0:
    print(0)
else:
    fibo[1] = 1
    for i in range(2, n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
        fibo[i] %= 1000000
    print(fibo[n])