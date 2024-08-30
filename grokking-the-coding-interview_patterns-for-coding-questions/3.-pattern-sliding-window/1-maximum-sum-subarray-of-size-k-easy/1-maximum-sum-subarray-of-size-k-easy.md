# 1.1 Maximum Sum Subarray of Size K \(easy\)
Locked under premium here [here](https://leetcode.com/problems/largest-subarray-length-k/description/)

#### Problem Statement

**Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.**

Example 1:

```text
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
```

Example 2:

```text
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
```

How can we solve the question?

We can think of the 'k' as window size of sliding window in an array.

1. With each slide we will remove an element from the left and add an element from the right.
2. Calculate the sum for that window and compare the sum of that window to prevous max sum of sliding windows.
3. **Beware:** Until the window size becomes equal to 'k', we have to just add the next element to the right but we shouldn't remove the element to the left.

So, code for that condition:

```java
public int maxSumOfContiguousSubArray(int arr[], int k) {
    int maxSum = 0; // It will keep the maximum Sum of the subarrays 
        // with the size 'k' and it will have the result by the end of the for-loop

    int windowSum = 0; // It will keep the sum of elements of that 
        // window till the current element

    int windowStart = 0; // Starting index of the window
    for(int windowEnd = 0; windowEnd < arr.length; windowEnd++) {
        // For each iteration ending of the window would be increase by 1.

        windowSum += arr[windowEnd]; //same as windowSum = windowSum + arr[windowEnd],
            // element to the right is added to the window so value of that element added 
            // with the previous elements within the window

        if(windowEnd >= k - 1) {
            // when the window size becomes equal to k(before that the size would less that k)

            maxSum = Math.max(maxSum, windowSum);
            // Taking the maximum value out of maxSum and the current window(i.e windowSum)

            windowSum -= arr[windowStart];
            // Removing the element from the left, windowStart is the starting index of the window;

            windowStart++;
            // windowStart is updated by 1 as the window slides to the right 
        }
    }
    return maxSum;
}
```

#### Time Complexity

The time complexity of the above algorithm will be O\(N\).

#### Space Complexity

The algorithm runs in constant space O\(1\).

