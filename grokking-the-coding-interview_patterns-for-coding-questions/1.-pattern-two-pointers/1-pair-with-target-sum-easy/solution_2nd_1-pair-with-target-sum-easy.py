def two_sum(nums, target):
    copy_nums = [*nums]
    copy_nums.sort()
    l = 0
    r = len(nums) - 1

    num1, num2 = 0, 0

    while l < r:
        curr_sum = copy_nums[l] + copy_nums[r]
        if target == curr_sum:
            num1, num2 = copy_nums[l], copy_nums[r]
            break
        elif curr_sum < target:
            l += 1
        else:
            r -= 1
    res = []
    for i in range(len(nums)):
        if len(res) < 2:
            if nums[i] == num1 or nums[i] == num2:
                res.append(i)

    return res
print(two_sum([2, 7, 11, 15], 9) == [0, 1])
print(two_sum([3, 2, 4], 6) == [1, 2])
print(two_sum([3, 3], 6)== [0, 1])
print(two_sum([2, 5, 5, 11], 10) == [1, 2])
