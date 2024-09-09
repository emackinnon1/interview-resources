# 3 Squaring a Sorted Array \(easy\)

https://leetcode.com/problems/squares-of-a-sorted-array/description/

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

This is a straightforward question. The only trick is that we can have negative numbers in the input array, which will make it a bit difficult to generate the output array with squares in sorted order.
An easier approach could be to first find the index of the first non-negative number in the array.
After that, we can use Two Pointers to iterate the array. One pointer will move forward to iterate
the non-negative numbers, and the other pointer will move backward to iterate the negative
numbers. At any step, whichever number gives us a bigger square will be added to the output array.
Since the numbers at both ends can give us the largest square, an alternate approach could be to
use two pointers starting at both ends of the input array. At any step, whichever pointer gives us
the bigger square, we add it to the result array and move to the next/previous number according to
the pointer.
 

Example 1:
```
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
```
Example 2:
```
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.