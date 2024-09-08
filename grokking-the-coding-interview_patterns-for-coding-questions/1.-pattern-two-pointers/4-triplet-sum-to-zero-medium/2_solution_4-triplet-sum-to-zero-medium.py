def triplet_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = len(nums) - 1

        while l < r:
            current_sum = nums[i] + nums[l] + nums[r]
            if current_sum == 0:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif current_sum < 0:
                l += 1
            else:
                r -= 1
    return result


print(triplet_sum([-3, 0, 1, 2, -1, 1, -2]))  # [[-3,1,2],[-2,0,2],[-2,1,1],[-1,0,1]]
print(triplet_sum([-5, 2, -1, -2, 3]))  # [[-5, 2, 3], [-2, -1, 3]]
print(triplet_sum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
print(triplet_sum([1, 2, -2, -1]))  # []
