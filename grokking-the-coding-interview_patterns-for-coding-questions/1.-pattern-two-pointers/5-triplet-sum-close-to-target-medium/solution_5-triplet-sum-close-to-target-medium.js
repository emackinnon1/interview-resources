const threeSumClosest = (nums, target) => {
    nums.sort((a, b) => a-b);
    let closest_sum = Infinity;

    for (let i = 0; i < nums.length - 2; i++) {
        l = i + 1;
        r = nums.length - 1;
        while (l < r) {
            current_sum = nums[i] + nums[l] + nums[r];
            if (target === current_sum) {
                return current_sum;
            }
            if (Math.abs(target-current_sum) < Math.abs(target-closest_sum)) closest_sum = current_sum;
            if (current_sum > 0) r--;
            else l++;
        }
    }
};