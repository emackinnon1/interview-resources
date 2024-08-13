def three_sum(nums):
    output = []
    nums.sort()
    h = 0
    i = 1
    j = 0


    print(nums)
    while i < len(nums) - 1:
        target = -nums[i]
        h = i - 1
        j = i + 1

        if nums[h] + nums[j] == target:
            print(i, h, j, nums)
            output.append([nums[h], nums[i], nums[j]])
            nums.pop(h)
            nums.pop(i)
            nums.pop(j)
        elif nums[h] + nums[j] < target:
            j += 1
        else:
            h += 1
        i += 1
    return output

print(three_sum([-3, 0, 1, 2, -1, 1, -2]))