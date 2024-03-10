def moveZeroes(nums: list[int]):
    zero_size = 0

    for i in range(len(nums)):
        num = nums[i]
        if num == 0:
            zero_size += 1
        else:
            if zero_size > 0:
                nums[i - zero_size] = num
                nums[i] = 0
        

nums = [1,0]

moveZeroes(nums)

print(nums)