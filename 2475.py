# BOJ _ 2475

nums = list(map(int, input().split()))

for i in range(len(nums)):
    nums[i] = nums[i] ** 2

print(sum(nums) % 10)