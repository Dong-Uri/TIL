n = int(input())
n -= 1
calc = []
while n > 1:
    if n % 2:
        calc.append(1)
        n -= 1
    else:
        calc.append(0)
        n //= 2
arr = [1, 1, 0]
for i in calc[::-1]:
    if i:
        arr = [(arr[0] + arr[1]) % 1000000007, arr[0], arr[1]]
    else:
        arr = [(arr[0] ** 2 + arr[1] ** 2) % 1000000007, (arr[1] * (arr[0] + arr[2])) % 1000000007, (arr[1] ** 2 + arr[2] ** 2) % 1000000007]
print(arr[0])