def has_33(nums):
    x = False
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1] and nums[i] == 3:
            x = True
    return x

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))