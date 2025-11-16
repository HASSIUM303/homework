def min_value(nums) -> int:
    M = nums[0]

    for i in range(len(nums)):
        if nums[i] < M: M = nums[i]


    return M


def sort_string(nums_str = ""):
    nums = nums_str.split(" ")
    nums.sort()
    result = ""

    for i in nums:
        result += i + " "

    return result
