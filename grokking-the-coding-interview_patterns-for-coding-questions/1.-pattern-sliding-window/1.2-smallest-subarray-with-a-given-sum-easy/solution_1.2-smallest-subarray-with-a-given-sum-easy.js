const minSubArralyLen = (target, nums) => {
    let windowStart = 0;
    let smallest = Infinity;
    let sum = 0;

    for (let windowEnd = 0; windowEnd < nums.length; windowEnd++) {
        sum += nums[windowEnd]
        while (sum >= target) {
            smallest = Math.min(smallest, windowEnd - windowStart + 1)
            sum -= nums[windowStart]
            windowStart++
        }
    }
    if (smallest === Infinity) return 0
    return smallest
}

console.log(minSubArralyLen(7, [2,3,1,2,4,3]) === 2)
console.log(minSubArralyLen(4, [1, 4, 4]) === 1)
console.log(minSubArralyLen(11, [1,1,1,1,1,1,1,1]) === 0)