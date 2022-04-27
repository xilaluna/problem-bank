# Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
# Example: a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],  t=20  ⇒  [13, 6] or [4, 17] or [5, 14]

a = [9, 13, 1, 8, 12, 4, 0, 5]
b = [3, 17, 4, 14, 6]
t = 20


def find_closest_pair(nums_1, nums_2, target):
    nums_1 = sorted(nums_1)
    nums_2 = sorted(nums_2)

    x, y, = 0, len(nums_2) - 1
    left, right = 0, len(nums_2) - 1

    while left < len(nums_1) and right >= 0:
        if abs(nums_1[left] + nums_2[right] - target) < abs(nums_1[x] + nums_2[y] - target):
            x = left
            y = right

        if nums_1[left] + nums_2[right] < target:
            left += 1

        elif nums_1[left] + nums_2[right] < target:
            right -= 1

        else:
            left += 1
            right -= 1

    return [nums_1[x], nums_2[y]]


print(find_closest_pair(a, b, t))
