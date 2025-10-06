nums = [1,2,0,6,8,9]
min_val = nums[0]
max_val = nums[0]

for i in nums:
    if i < min_val:
        min_val = i
    if i > max_val:
        max_val = i
print(min_val)
print(max_val)