def consecutive(nums, a, b):
    unique = [a, b]
    tof = False
    for i in range(len(nums)-1):
        if i in unique:
            if nums[i+1] in unique:
                tof = True
            if nums[i-1] in unique:
                tof = True
    return tof
