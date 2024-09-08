# 4 Triplet Sum to Zero \(medium\)

https://leetcode.com/problems/3sum/
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
```
Example 2:
```
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```
Example 3:
```
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

> Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
This problem follows the Two Pointers pattern and shares similarities with Pair with Target Sum.
A couple of differences are that the input array is not sorted and instead of a pair we need to find
triplets with a target sum of zero.
To follow a similar approach, first, we will sort the array and then iterate through it taking one
number at a time. Letʼs say during our iteration we are at number ‘X’ , so we need to find ‘Y’ and
‘Z’ such that X + Y + Z == 0 . At this stage, our problem translates into finding a pair whose
sum is equal to “-X” (as from the above equation Y + Z == -X ).
Another difference from Pair with Target Sum is that we need to find all the unique triplets. To
handle this, we have to skip any duplicate number. Since we will be sorting the array, so all the
duplicate numbers will be next to each other and are easier to skip.


- sort the nums
- initialize a res list
- start a for loop
    - first thing to do in the for loop is check that the previous i is not the same as the current i (also check to be sure that i > 0)
    - if it is continue
    - initialize left and right pointers (l = i +1, r = nums.length -1)
    - start a while loop with condition that l is less than r
        - initialize total of i, left and right pointers
        - if total is 0, append to results list
            - 
            - start another while loop here with conditions of left pointer == left pointer - 1 and left pointer less than right pointer 
        - if total is less than 0, increase left pointer
        - if total is less than 0, decrement right pointer
