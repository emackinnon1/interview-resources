# 1.2 Smallest Subarray with a given sum \(easy\)
Solved in JS [here](https://leetcode.com/problems/minimum-size-subarray-sum/description/)

### Problem Statement

**Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.**

Example 1:

```text
Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum greater than 
or equal to '7' is [5, 2].
```

Example 2:

```text
Input: [2, 1, 5, 2, 8], S=7
Output: 1
Explanation: The smallest subarray with a sum greater than 
or equal to '7' is [8].
```

Example 3:

```text
Input: [3, 4, 1, 1, 6], S=8
Output: 3
Explanation: Smallest subarrays with a sum greater than 
or equal to '8' are [3, 4, 1] or [1, 1, 6].
```

### Solution

This problem follows the Sliding Window pattern, and we can use a similar strategy as discussed in Maximum Sum Subarray of Size K. There is one difference though: in this problem, the sliding window size is not fixed. Here is how we will solve this problem:

1. First, we will add-up elements from the beginning of the array until their sum becomes greater than or equal to ‘S.’
2. These elements will constitute our sliding window. We are asked to find the smallest such window having a sum greater than or equal to ‘S.’ We will remember the length of this window as the smallest window so far.
3. After this, we will keep adding one element in the sliding window \(i.e., slide the window ahead\) in a stepwise fashion.
4. In each step, we will also try to shrink the window from the beginning. We will shrink the window until the window’s sum is smaller than ‘S’ again. This is needed as we intend to find the smallest window. This shrinking will also happen in multiple steps; in each step, we will do two things:
   * Check if the current window length is the smallest so far, and if so, remember its length.
   * Subtract the first element of the window from the running sum to shrink the sliding window.

```java
public int smallestSubarrayWithGivenSum(int arr[], int S) {
   int minLen = Integer.MAX_VALUE;
   // it will hold the size of smallest subarray
   // Integer.MAX_VALUE is the greatest number a int can hold
   // we need the minimum length/size so we will compare others with it. 
   int windowSum = 0, windowStart = 0;
   // windowSum holds sum of the elements in that window
   // windowStart holds the starting position of current window
 
   for(int windowSize = 0; windowSize < arr.length; windowSize++) {
       // iterating through every element using windowEnd
       windowSum += arr[windowSize];
       // element is added to the window
       while(windowSum >= S) {
         // while windowSum is greater than equal to S
            minLen = Math.min(minLen, windowEnd - windowStart + 1);
           // compares min len of window with the current window
            windowSum -= arr[windowStart];
           // removing the element at the start of the window
            windowStart++;
           // moving the window start position to the next place
       }
   }
   
   return minLen == Integer.MAX_VALUE ? 0 : minLen;
   // ternary operator:
   // if minLen is equal to Integer.MAX_VALUE means minimun window
   // with given sum greater than equal to S is not there. So, it
   // return 0 else it return minLen
}
```

#### Time Complexity

The time complexity of the above algorithm will be O\(N\). The outer for loop runs for all elements, and the inner while loop processes each element only once; therefore, the time complexity of the algorithm will be O\(N+N\), which is asymptotically equivalent to O\(N\).

#### Space Complexity

The algorithm runs in constant space O\(1\).

