nums = list(range(0,101))
nums.remove(5)
def missing_no(nums):
    c = 0
    for i in range(len(nums)):
        while nums[i] == c:
            c = c + 1
    return c