# Given an array a of n numbers and a count k find the k largest values in the array a.
# Example: a = [5, 1, 3, 6, 8, 2, 4, 7], k = 3  ⇒  [6, 8, 7]

a = [5, 1, 3, 6, 8, 2, 4, 7]
k = 3


def largest_nums(list, nums):
    arr = []
    list.sort(reverse=True)
    for i in range(nums):
        arr.append(list[i])

    return arr


print(largest_nums(a, k))
