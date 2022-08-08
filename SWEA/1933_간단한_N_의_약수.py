N = int(input())

for i in range(1,N): # 1부터 N-1까지
    if N % i == 0: # 나눠진다면 == 약수라면
        print(i, end=' ')
print(N)