N = int(input())
nums = [int(x) for x in input().split()]
nums.sort()
print(nums[int((N-1)/2)])