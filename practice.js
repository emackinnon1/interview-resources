// Input: [2, 1, 5, 1, 3, 2], k=3 
// Output: 9
// Explanation: Subarray with maximum sum is [5, 1, 3]

function maxSumSubarraySizeK(arr, k) {
    let windowStart = 0;
    let sum = 0;
    let results = []

    for (let windowEnd = 0; windowEnd < arr.length; windowEnd++) {
        sum += arr[windowEnd]
        if (windowEnd >= k - 1) {
            results.push(sum)
            sum -= arr[windowStart]
            windowStart++
        }
    }
    return Math.max(...results)

}

console.log(maxSumSubarraySizeK([2, 3, 4, 1, 5], 2))