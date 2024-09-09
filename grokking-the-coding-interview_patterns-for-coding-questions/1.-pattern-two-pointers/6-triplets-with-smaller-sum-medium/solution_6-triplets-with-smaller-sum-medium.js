const tripletSmallerSum = (nums, target) => {
    nums.sort((a, b) => a-b);
    let count = 0;
    for (let i = 0; i < nums.length - 2; i++) {
        let l = i + 1;
        let r = nums.length - 1;
        let current = nums[i] + nums[l] + nums[r];
        while (l < r) {
            if (current < target) {
                count++;
                l++;
            } else {
                r--;
            }
        }
    }
    return count;

}

console.log(tripletSmallerSum([-2,0,1,3], 2));
console.log(tripletSmallerSum([-2,0,-1,3], 2));
console.log(tripletSmallerSum([3, 1, 0, 2], 5));