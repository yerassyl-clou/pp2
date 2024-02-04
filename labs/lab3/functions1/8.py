def spy_game(nums):
    cond1, cond2, cond3 = False, False, False

    for i in range(len(nums)):
        if nums[i] == 0:
            cond1 = True
        if nums[i] == 0 and cond1:
            cond2 = True
        if nums[i] == 7 and cond1 and cond2:
            return True
    
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))