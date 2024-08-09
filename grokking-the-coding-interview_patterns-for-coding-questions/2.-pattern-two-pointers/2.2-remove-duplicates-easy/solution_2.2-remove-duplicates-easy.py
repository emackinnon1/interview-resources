def remove_dupes(nums):
    k = 1
    i = 1

    while i < len(nums):
        if nums[k-1] != nums[i]:
            nums[k] = nums[i]
            k += 1

        i += 1

    return nums, k


res1arr, resk1 = remove_dupes([1, 1, 1])
res2arr, resk2 = remove_dupes([1, 1, 2])
res3arr, resk3 = remove_dupes([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])

def test(arr, k):
    deduped = list(set(arr))
    return deduped == arr[:k]

print(test(res1arr, resk1))
print(test(res2arr, resk2))
print(test(res3arr, resk3))
