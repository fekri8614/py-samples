def find_max(nums):
    max_num = float("-inf")
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


numbers = [1, 2, 3, 10]
print(find_max(numbers))
