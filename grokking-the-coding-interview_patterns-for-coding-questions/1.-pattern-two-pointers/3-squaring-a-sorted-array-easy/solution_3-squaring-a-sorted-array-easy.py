def sorted_squares(nums):
    # res = []
    # for n in nums:
    #     res.append(n * n)
    # res.sort()
    # return res
    start = 0
    end = len(nums) - 1
    highestIndex = len(nums) - 1
    output = [*range(len(nums))]


    while start < end:
        startSquare = nums[start] * nums[start]
        endSquare = nums[end] * nums[end]
        if startSquare > endSquare:
            output[highestIndex] = startSquare
            start += 1
        else:
            output[highestIndex] = endSquare
            end -= 1
        highestIndex -= 1
    return output


print(sorted_squares([-2, -1, 0, 2, 3]) == [0, 1, 4, 4, 9])
print(sorted_squares([-3, -1, 0, 1, 2]) == [0, 1, 1, 4, 9])
