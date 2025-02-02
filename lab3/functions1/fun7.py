def has_33(nums):
    check = False
    for i in range(0, len(nums) - 1):
        if(nums[i] == nums[i+1] == 3):
            check = True
            break
    return check

print(has_33([1, 3, 3])) #→ True
print(has_33([1, 3, 1, 3])) #→ False
print(has_33([3, 1, 3])) #→ False