def three_sum_smaller(nums, target): 
    nums.sort()

    count = []

    for i in range(len(nums) - 1):
        l = i + 1
        r = len(nums) - 1
        curr_sum = nums[i] + nums[l] + nums[r]

        while l < r:
            if curr_sum < target:
                count.append([nums[i], nums[l], nums[r]])
                l += 1
            else:
                r -= 1

    return len(count)


print(three_sum_smaller([-2, 0, 1, 3], 2)) #2
print(three_sum_smaller([-2, 0, -1, 3], 2)) #2
print(three_sum_smaller([3, 1, 0, 2], 5)) #2
