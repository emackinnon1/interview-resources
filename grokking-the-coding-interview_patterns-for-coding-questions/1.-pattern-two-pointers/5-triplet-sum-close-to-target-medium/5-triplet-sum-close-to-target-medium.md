# 5 Triplet Sum Close to Target \(medium\)

- sort the numbers to make traversing easier
- initiate the closest var as Infinity
- iterate over the array, stopping at the second to last number (length - 2) since the rightward pointer will cover that one.
- while left pointer is less than right pointer,
- add up the current triplet.
- If the current triplet equals the target triplet, return.
- If the target - current triplet is less than the closest sum var, set the closest sum var to the current triplet
- if the current triplet is less than the target, we need to move the leftward pointer
- if the current triplet is larger than the target, we need to move the rightward pointer