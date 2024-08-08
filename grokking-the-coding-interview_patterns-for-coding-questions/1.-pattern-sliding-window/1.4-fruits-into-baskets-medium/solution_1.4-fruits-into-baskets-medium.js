const totalFruit = (fruits) => {
    let largest = 0;
    let fMap = {};
    let start = 0;

    fruits.forEach((f, end) => {
        if (!fMap[f]) {
            fMap[f] = 0
        }
        fMap[f]++;
        while (Object.keys(fMap).length > 2) {
            const firstIn = fruits[start];
            fMap[firstIn]--
            if (fMap[firstIn] === 0) {
                delete fMap[firstIn]
            }
            start ++
        }
        largest = Math.max(largest, end - start + 1);
    });
    return largest;
}

console.log(totalFruit([1,2,1]) === 3)
console.log(totalFruit([0,1,2,2]) === 3)
console.log(totalFruit([1,2,3,2,2]) === 4)
console.log(totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) === 5)