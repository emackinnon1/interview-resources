# 6 Triplets with Smaller Sum \(medium\)

## Description
Given an array of n integers nums and a target, find the number of index triplets `i, j, k` with `0 <= i < j < k < n` that satisfy the condition `nums[i] + nums[j] + nums[k] < target`.

## Example
### Example1

```
Input:  nums = [-2,0,1,3], target = 2
Output: 2
Explanation:
Because there are two triplets which sums are less than 2:
[-2, 0, 1]
[-2, 0, 3]
```

### Example2

```
Input: nums = [-2,0,-1,3], target = 2
Output: 3
Explanation:
Because there are three triplets which sums are less than 2:
[-2, 0, -1]
[-2, 0, 3]
[-2, -1, 3]
```

- sort nums
- initialize count at 0
- iterate through array in for loop
    - initialize left and right pointers (i + 1 and nums.length - 1, respectively) and current sum (i + l + r indexes in nums)
    - inner while (l < r) block
        - if current sum is less than target
            - increase count and left pointer
        - else decrement right pointer