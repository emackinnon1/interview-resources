def totalFruit(fruits):
    fruit_map = {}
    start = 0

    for end, fruit in enumerate(fruits):
        if fruit not in fruit_map:
            fruit_map[fruit] = 1
        else:
            fruit_map[fruit] += 1
        while len(fruit_map.keys()) > 2:
            fruit_map[fruits[start]] -= 1
            if fruit_map[fruits[start]] < 1:
                del fruit_map[fruits[start]]
            start += 1
    count = 0
    for val in fruit_map.values():
        count += val
    return count

print(totalFruit([1,2,1]))
print(totalFruit([0,1,2,2]))
print(totalFruit([1,2,3,2,2]))
