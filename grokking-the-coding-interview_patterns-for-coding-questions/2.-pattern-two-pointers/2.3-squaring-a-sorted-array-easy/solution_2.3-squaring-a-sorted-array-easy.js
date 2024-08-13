const sortSquares = (nums) => {
    const n = nums.length;
    let start = 0;
    let end = n - 1;
    let highestIndex = n - 1;
    let squares = Array(n).fill(0);

    while (start < end) {
        let startSquare = nums[start] * nums[start];
        let endSquare = nums[end] * nums[end];

        if (startSquare > endSquare) {
            squares[highestIndex] = startSquare
            start ++
        } else {
            squares[highestIndex] = endSquare
            end--
        }
        highestIndex--
    }

    return squares
}

console.log(sortSquares([-2, -1, 0, 2, 3]))//[0, 1, 4, 4, 9]
console.log(sortSquares([-3, -1, 0, 1, 2]))//[0, 1, 1, 4, 9]