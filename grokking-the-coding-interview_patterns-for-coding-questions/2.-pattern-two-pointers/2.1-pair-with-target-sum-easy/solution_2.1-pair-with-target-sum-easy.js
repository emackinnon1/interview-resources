const twoSum = (nums, target) => {
    // let start = 0;
    // let end = nums.length - 1;

    // let copy = [...nums];

    // while (start < end) {
    //     let current = target - nums[start];
    //     if (current === nums[end]) return [start, end];
    //     else if (current > nums[end]) start++;
    //     else if (current < nums[end]) end--;
    // }
    // return [start, end]
    let hash = {}
    let answer = []
    
    nums.forEach((n, i) => {
        if (target - n in hash) {
            answer = [hash[target - n], i];
        }
        hash[n] = i;
    });
    return answer
}


const test = (inputsArr, result) => {
    const [nums, target] = inputsArr;
    return twoSum(nums, target).every((val, i) => val == result[i])
};


const res1 = test([[2, 7, 11, 15], 9], [0, 1])
const res2 = test([[3,2,4], 6], [1, 2])
const res3 = test([[3,3], 6], [0, 1])
const res4 = test([[2,5,5,11], 10], [1, 2])


console.log(res1);
console.log(res2);
console.log(res3);
console.log(res4);