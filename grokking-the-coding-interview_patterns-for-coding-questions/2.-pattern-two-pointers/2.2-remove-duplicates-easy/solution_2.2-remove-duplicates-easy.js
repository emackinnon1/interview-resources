function removeDupes(arr) {
    k = 1
    i = 1

    while (i < arr.length) {
        if (arr[k - 1] !== arr[i]) {
            arr[k] = arr[i]
            k++
        }
        i++
    }
    return [arr, k]
}

const test = (arr, k) => {
    deduped = [...new Set(arr)] 
    return deduped.every((n, i) => n === arr[i])
}

const [resArr1, k1] = removeDupes([2, 3, 3, 3, 6, 9, 9])
const [resArr2, k2] = removeDupes([2, 2, 2, 11])

console.log(test(resArr1, k1))
console.log(test(resArr2, k2))