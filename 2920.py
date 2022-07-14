# BOJ _ 2920 _ 음계

nums = list(map(int, input().split()))
reversenums = sorted(nums, reverse = True)
if sorted(nums) == nums:
    print("ascending")
elif reversenums == nums:
    print("descending")
else:
    print("mixed")