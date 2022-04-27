# Two Sum II - Input Array Is Sorted.
# Given a 1-indexed array of integers numbers that are already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.

numbers = [2, 7, 11, 15]
target = 9


def sortedTwoSum(nums, t):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum > t:
            right -= 1
        elif current_sum < t:
            left += 1
        else:
            return [left, right]


print(sortedTwoSum(numbers, target))
