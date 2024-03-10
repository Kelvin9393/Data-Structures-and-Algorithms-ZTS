def rotate(nums: list[int], k: int):
    k = k % len(nums)
    l, r = 0, len(nums) - 1

    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)

def reverse(array, start, end):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start, end = start + 1, end - 1


nums = [1,2,3,4,5,6,7]

rotate(nums, 3)

print(nums)