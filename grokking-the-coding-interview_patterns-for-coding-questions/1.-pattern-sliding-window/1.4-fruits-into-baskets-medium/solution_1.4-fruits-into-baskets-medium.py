def total_fruit(fruits):
    fruit_map = {}
    max_length = 0
    start = 0

    for end, fruit in enumerate(fruits):
        if fruit not in fruit_map:
            fruit_map[fruit] = 0
        fruit_map[fruit] += 1
        while len(fruit_map.keys()) > 2:
            fruit_map[fruits[start]] -= 1
            if fruit_map[fruits[start]] == 0:
                del fruit_map[fruits[start]]
            start += 1
        curr_window = end - start + 1
        max_length = curr_window if curr_window > max_length else max_length
    return max_length

print(total_fruit([1,2,1]) == 3)
print(total_fruit([0,1,2,2]) == 3)
print(total_fruit([1,2,3,2,2]) == 4)
print(total_fruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5)
