# Given an array a of n numbers and a target value t, find two numbers whose sum is t.
# Example: a = [5, 3, 6, 8, 2, 4, 7], t = 10  ⇒  [3, 7] or [6, 4] or [8, 2]

a = [5, 3, 6, 8, 2, 4, 7]
t = 10


def two_sum(target, nums):
    hash_map = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in hash_map:
            return [nums[hash_map[diff]], nums[i]]
        hash_map[n] = i
    return


print(two_sum(t, a))
