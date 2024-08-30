def two_sum(nums, target):
    num_map = {}

    for i, n in enumerate(nums):
        if target - n in num_map:
            return [num_map[target-n], i]
        num_map[n] = i

print(two_sum([2, 7, 11, 15], 9) == [0, 1])
print(two_sum([3,2,4], 6) == [1, 2])
print(two_sum([3,3], 6) == [0, 1])
print(two_sum([2,5,5,11], 10) == [1, 2])
