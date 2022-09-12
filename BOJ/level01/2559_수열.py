N, K = map(int, input().split())
lst = list(map(int, input().split()))
temp_sum = 0
for i in range(K):
    temp_sum += lst[i]
max_temp_sum = temp_sum
for i in range(N-K):
    temp_sum = temp_sum - lst[i] + lst[i+K]
    if temp_sum > max_temp_sum:
        max_temp_sum = temp_sum
print(max_temp_sum)