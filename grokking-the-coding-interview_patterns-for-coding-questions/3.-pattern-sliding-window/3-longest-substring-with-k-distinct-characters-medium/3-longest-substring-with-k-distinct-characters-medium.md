# 1.3 Longest Substring with K Distinct Characters \(medium\)
Locked under premium [here](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/)

#### Problem Statement

Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

```text
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more 
than '2' distinct characters is "araa".
```

Example 2:

```text
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more 
than '1' distinct characters is "aa".
```

Example 3:

```text
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more 
than '3' distinct characters are "cbbeb" & "bbebi".
```

#### Solution

This problem follows the Sliding Window pattern, and we can use a similar dynamic sliding window strategy as discussed in Smallest Subarray with a given sum. We can use a HashMap to remember the frequency of each character we have processed. Here is how we will solve this problem:

1. First, we will insert characters from the beginning of the string until we have ‘K’ distinct characters in the HashMap.
2. These characters will constitute our sliding window. We are asked to find the longest such window having no more than ‘K’ distinct characters. We will remember the length of this window as the longest window so far.
3. After this, we will keep adding one character in the sliding window \(i.e., slide the window ahead\) in a stepwise fashion.
4. In each step, we will try to shrink the window from the beginning if the count of distinct characters in the HashMap is larger than ‘K.’ We will shrink the window until we have no more than ‘K’ distinct characters in the HashMap. This is needed as we intend to find the longest window.
5. While shrinking, we’ll decrement the character’s frequency going out of the window and remove it from the HashMap if its frequency becomes zero.
6. At the end of each step, we’ll check if the current window length is the longest so far, and if so, remember its length.

**Source code**

```java
public int longestSubstringWithKDistinctChars(String s, int k) {

    if(s == null || s.length == 0 || k == 0) return 0;
    int windowStart - 0;
    int maxLen = 0;
    Map<Character, Integer> mp = new HashMap<>();
    
    for(int windowEnd = 0; windowEnd < s.length(); windowEnd++) {
        char right = s.charAt(windowEnd);
        mp.put(right, mp.getOrDefault(right, 0) + 1);
        
        while(mp.size > k) {
            char left = s.chartAt(windowStart);
            mp.put(left, mp.get(left) - 1);
            if(mp.get(left) == 0) {
                mp.remove(left);
            }
            windowStart++;
        }
        maxLen = Math.max(maxLen, windowEnd - windowStart + 1);
    }
    return maxLen;
}
```

#### Time Complexity

The above algorithm’s time complexity will be O\(N\), where ‘N’ is the number of characters in the input string. The outer for loop runs for all characters, and the inner while loop processes each character only once; therefore, the time complexity of the algorithm will be O\(N+N\)O\(N+N\), which is asymptotically equivalent to O\(N\).

#### Space Complexity

The algorithm’s space complexity is O\(K\), as we will be storing a maximum of ‘K+1’ characters in the HashMap.

