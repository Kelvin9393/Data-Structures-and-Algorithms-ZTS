nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums: list[int]) -> int:
        maximum = maxarray = nums[0]
        for i in range(1, len(nums)):
            print(f"###### {i} ######")
            print(nums[i])
            print(nums[i], maxarray+nums[i])
            print(maxarray)
            maxarray = max(nums[i], maxarray+nums[i])
            maximum = max(maxarray, maximum)
        return maximum

print(maxSubArray(nums))