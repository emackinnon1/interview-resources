# 1 Pair with Target Sum (easy)

Given an array of integers `nums` and an integer `target`, return _indices of the two numbers such that they add up to `target`_.

You may assume that each input would have _**exactly**_** one solution**, and you may not use the _same_ element twice.

You can return the answer in any order.

**Example 1:**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

**Constraints:**

* `2 <= nums.length <= 104`
* `-109 <= nums[i] <= 109`
* `-109 <= target <= 109`
* **Only one valid answer exists.**

&#x20; **Follow-up:** Can you come up with an algorithm that is less than `O(n2)` time complexity?

**Solution:**

### **Method 1:** Brute Force

This approach is straightforward. We can check for every pair in the array and if their sum is equal to the given target, print their indices. This kind of [Brute Force](https://en.wikipedia.org/wiki/Brute-force\_search) solution needs to check every possible pair and number of possible pairs in the array = **n \* (n – 1) / 2.** So, in the worst-case, this approach can be slow.

![](<../.gitbook/assets/image (3).png>)

1. Run a loop to maintain the first index of the solution in the array
2. Run another loop to maintain a second index of the solution for every first integer
3. If at any point, the sum of values of two indices is equal to the target
   * Print its indices

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i = 0 ; i < nums.length - 1 ; i++)
            for(int j = i + 1 ; j < nums.length ; j++) {
                if(nums[i] + nums[j] == target)
                    return new int[]{i , j};
            }
        return new int[]{-1 , -1};
    }
}
```

#### Complexity Analysis:

**Time Complexity**

**O(N \* N),** where N =  size of the array. As we check for possible pair, and the total number of pairs are: **N \* (N – 1) / 2.**

**Space complexity**

**O(1)**. Only constant space for variables is used.

### **Method 2: Using Sorting**

We can get some advantage if the array is already sorted. An approach to solve the problem would be:

* Sort the given array.
* Start two pointers. Pointer A starts from the beginning of the array, such that it points to the smallest element. Pointer B starts from the end of the array, pointing at the maximum element of the array.
* Now, start a while loop `while(pointer A < pointer B)`
* Get a sum of the elements at `pointerA` and `pointerB`.
* This is where the magic comes in. If the sum is less than `target`, it simply means that we need to add a bigger number. Hence move the `pointerA` one step ahead. Else, we need a smaller number, and we can move the `pointerB` one step backward.
* Somewhere along this iteration, we will get our desired indices.

```java
  int[] twoSumSorting(int[] nums, int target) {
    int[] copyArray = Arrays.copyOf(nums, nums.length);
    Arrays.sort(copyArray);

    int head = 0;
    int tail = copyArray.length - 1;
    int num1 = 0, num2 = 0;
    while (head < tail) {
      int sum = copyArray[head] + copyArray[tail];
      if (sum < target) {
        head++;
      }
      else if (sum > target) {
        tail--;
      } else {
        num1 = copyArray[head];
        num2 = copyArray[tail];
        break;
      }
    }

    // Create the result array with indices
    int[] result = new int[2];
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] == num1) result[0] = i;
      if (nums[i] == num2) result[1] = i;
    }
    return result;
  }
```

![Image showing solution using sorting](https://i2.wp.com/studyalgorithms.com/wp-content/uploads/2021/01/Screenshot-2021-01-10-040252.png?resize=1024%2C672\&ssl=1)

The above method works in a time complexity of O(n∗log⁡n) because of the sorting step involved. You can use a [quick sort algorithm](https://studyalgorithms.com/array/quick-sort/) to sort your array.

### **Method 3: Use Hashing**

In the previous method, we did not use extra space and achieved a decent time complexity. But, if you can allow yourself to compromise on some space, you can solve this problem in an even efficient manner.

Instead of finding two numbers whose sum equal to a `target` value, we can think of the problem in an alternative way:

_**target\_value − first\_number = second\_number**_

So, we can develop an algorithm in the following way:

* Initialize a hash-table that will store the index and the element.
* Start to traverse the array.
* For each element in the array use the above define formula to find the complementing number.
* Look up the complementing number in the hash table. If found, return the `2` indices.
* Else, add the element along with its index to the hash table and proceed with the other elements.

![Image showing solution using a hash-table](https://i2.wp.com/studyalgorithms.com/wp-content/uploads/2021/01/Screenshot-2021-01-10-040039.png?resize=1024%2C675\&ssl=1)

**Implementation:**

```java
  int[] twoSumHashing(int[] nums, int target) {

    // Create a HashMap
    Map<Integer, Integer> map = new HashMap<>();

    for (int i = 0; i < nums.length; i++) {

      // Get the complement using the target value
      int complement = target - nums[i];

      // Search the hashmap for complement, if found, we got our pair
      if (map.containsKey(complement)) {
        return new int[]{map.get(complement), i};
      }

      // Put the element in hashmap for subsequent searches.
      map.put(nums[i], i);
    }
    throw new IllegalArgumentException("No two sum solution");
  }
```

_Time Complexity:_ O(n)\
_Space Complexity:_ O(n)
