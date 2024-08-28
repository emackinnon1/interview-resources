def three_sum(nums):
    triplets = []
    nums.sort()

    for h, n in enumerate(nums):
        if h > 0 and nums[h] == nums[h-1]:
            continue
        i = h + 1
        j = len(nums) - 1
        while i <= j:
            curr_target = -n
            res = [nums[i], nums[j], nums[h]]
            res.sort()
            if nums[i] + nums[j] == curr_target:
                if (
                    i != j != h != i
                ):
                    triplets.append(res)
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i-1]:
                    i += 1
                while i < j and nums[j] == nums[j+1]:
                    j -= 1
            elif nums[i] + nums[j] < curr_target:
                i += 1
            else:
                j -= 1

    return triplets

print(three_sum([-3, 0, 1, 2, -1, 1, -2]))  # [[-3,1,2],[-2,0,2],[-2,1,1],[-1,0,1]]
print(three_sum([-5, 2, -1, -2, 3])) #[[-5, 2, 3], [-2, -1, 3]]
print(three_sum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
print(three_sum([1, 2, -2, -1]))  # []


def triplets(nums):
    res = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        j = i + 1
        k = len(nums) - 1

        while j < k:
            total = nums[i] + nums[j] + nums[k]

            if total > 0:
                k -= 1
            elif total < 0:
                j += 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j += 1

                while nums[j] == nums[j-1] and j < k:
                    j += 1
    
    return res